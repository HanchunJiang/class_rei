/** @file class.c
 * Julien Lesgourgues, 17.04.2011
 */

#include "class.h"
int calculate_derivative(struct perturbations *ppt, struct transfer *ptr, int index_q_now, int *index_q_next, int index_n, double alpha, double k_0, double *results){
  double next_k=k_0*pow(alpha,index_n);
  double pi=3.1415926;
  int index_q=index_q_now;
  int l_size=ptr->l_size[ppt->index_md_tensors];
  for(int i=0;i<l_size;i++)results[i]=0;
  for(;index_q<ptr->q_size&&ptr->q[index_q]<next_k;index_q++){
    for(int index_l=0;index_l<l_size;index_l++){
      double transfer=0;
      transfer_functions_at_q_l(ptr,ppt->index_md_tensors,ppt->index_ic_ad,ptr->index_tt_b,index_l,index_q,&transfer);
      double temp=4*pi*pow(transfer,2)/ptr->q[index_q]*(ptr->q[index_q+1]-ptr->q[index_q]);
      results[index_l]+=temp;
    }
  }
  //printf("test=%e\n",results[30]);
  *index_q_next=index_q;
  return _SUCCESS_;
}

int my_fun(struct perturbations *ppt, struct transfer *ptr){
  double k_0=0.0001;
  double k_n=0.03;
  double alpha=2.04;
  int N_max=8;
  int index_n=1;

  printf("index_md_tensor=%d\n",ppt->index_md_tensors);
  printf("index_ic_ad=%d\n",ppt->index_ic_ad);
  printf("index_tt_b=%d\n",ptr->index_tt_b);
  printf("l_size[index_md_tensor]=%d\n",ptr->l_size[ppt->index_md_tensors]);

  double transfer=100;
  double *transfers[8];
  for(int i=0;i<8;i++) 
    transfers[i] = (double *)malloc( ptr->l_size[ppt->index_md_tensors] * sizeof(double) );
  FILE *fp;
      fp = fopen("/home/hcjiang/class/transfer_function.txt","w+");
  int index_q_start=0;
  int index_q_end=0;
  for (;ptr->q[index_q_start]<k_0;)index_q_start++;//寻找到开始积分的k的index在哪里
  printf("%d\n",index_q_start);
  for(;index_n<=N_max;index_n++)calculate_derivative(ppt,ptr,index_q_start,&index_q_end,index_n,alpha,k_0,transfers[index_n-1]);
  printf("test=%e\n",transfers[3][15]);
  //fprintf(fp,"l=%d,q=%f,transfer_function=%f\n",ptr->l[index_l],ptr->q[index_q],transfer);
  fclose(fp);
   for(int i=0;i<8;i++) free(transfers[i]); 
  return _SUCCESS_;
}

int main(int argc, char **argv) {

  struct precision pr;        /* for precision parameters */
  struct background ba;       /* for cosmological background */
  struct thermodynamics th;           /* for thermodynamics */
  struct perturbations pt;         /* for source functions */
  struct primordial pm;       /* for primordial spectra */
  struct fourier fo;        /* for non-linear spectra */
  struct transfer tr;        /* for transfer functions */
  struct harmonic hr;          /* for output spectra */
  struct lensing le;          /* for lensed spectra */
  struct distortions sd;      /* for spectral distortions */
  struct output op;           /* for output files */
  ErrorMsg errmsg;            /* for error messages */

  if (input_init(argc, argv,&pr,&ba,&th,&pt,&tr,&pm,&hr,&fo,&le,&sd,&op,errmsg) == _FAILURE_) {
    printf("\n\nError running input_init \n=>%s\n",errmsg);
    return _FAILURE_;
  }

  if (background_init(&pr,&ba) == _FAILURE_) {
    printf("\n\nError running background_init \n=>%s\n",ba.error_message);
    return _FAILURE_;
  }

  if (thermodynamics_init(&pr,&ba,&th) == _FAILURE_) {
    printf("\n\nError in thermodynamics_init \n=>%s\n",th.error_message);
    return _FAILURE_;
  }

  if (perturbations_init(&pr,&ba,&th,&pt) == _FAILURE_) {
    printf("\n\nError in perturbations_init \n=>%s\n",pt.error_message);
    return _FAILURE_;
  }

  if (primordial_init(&pr,&pt,&pm) == _FAILURE_) {
    printf("\n\nError in primordial_init \n=>%s\n",pm.error_message);
    return _FAILURE_;
  }

  if (fourier_init(&pr,&ba,&th,&pt,&pm,&fo) == _FAILURE_) {
    printf("\n\nError in fourier_init \n=>%s\n",fo.error_message);
    return _FAILURE_;
  }

  if (transfer_init(&pr,&ba,&th,&pt,&fo,&tr) == _FAILURE_) {
    printf("\n\nError in transfer_init \n=>%s\n",tr.error_message);
    return _FAILURE_;
  }

  if (harmonic_init(&pr,&ba,&pt,&pm,&fo,&tr,&hr) == _FAILURE_) {
    printf("\n\nError in harmonic_init \n=>%s\n",hr.error_message);
    return _FAILURE_;
  }

  if (lensing_init(&pr,&pt,&hr,&fo,&le) == _FAILURE_) {
    printf("\n\nError in lensing_init \n=>%s\n",le.error_message);
    return _FAILURE_;
  }

  if (distortions_init(&pr,&ba,&th,&pt,&pm,&sd) == _FAILURE_) {
    printf("\n\nError in distortions_init \n=>%s\n",sd.error_message);
    return _FAILURE_;
  }

  if (output_init(&ba,&th,&pt,&pm,&tr,&hr,&fo,&le,&sd,&op) == _FAILURE_) {
    printf("\n\nError in output_init \n=>%s\n",op.error_message);
    return _FAILURE_;
  }
  
  /****** all calculations done, now free the structures ******/
  my_fun(&pt,&tr);

  if (distortions_free(&sd) == _FAILURE_) {
    printf("\n\nError in distortions_free \n=>%s\n",sd.error_message);
    return _FAILURE_;
  }

  if (lensing_free(&le) == _FAILURE_) {
    printf("\n\nError in lensing_free \n=>%s\n",le.error_message);
    return _FAILURE_;
  }

  if (harmonic_free(&hr) == _FAILURE_) {
    printf("\n\nError in harmonic_free \n=>%s\n",hr.error_message);
    return _FAILURE_;
  }

  if (transfer_free(&tr) == _FAILURE_) {
    printf("\n\nError in transfer_free \n=>%s\n",tr.error_message);
    return _FAILURE_;
  }

  if (fourier_free(&fo) == _FAILURE_) {
    printf("\n\nError in fourier_free \n=>%s\n",fo.error_message);
    return _FAILURE_;
  }

  if (primordial_free(&pm) == _FAILURE_) {
    printf("\n\nError in primordial_free \n=>%s\n",pm.error_message);
    return _FAILURE_;
  }

  if (perturbations_free(&pt) == _FAILURE_) {
    printf("\n\nError in perturbations_free \n=>%s\n",pt.error_message);
    return _FAILURE_;
  }

  if (thermodynamics_free(&th) == _FAILURE_) {
    printf("\n\nError in thermodynamics_free \n=>%s\n",th.error_message);
    return _FAILURE_;
  }

  if (background_free(&ba) == _FAILURE_) {
    printf("\n\nError in background_free \n=>%s\n",ba.error_message);
    return _FAILURE_;
  }

  return _SUCCESS_;

}
