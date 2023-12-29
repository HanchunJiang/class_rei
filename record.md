# 计算$\chi^2$
* 算正确的$C_l$
    * 用`reio_camb`
    * 结果存在`reio_camb04`
* 算错误的$C_l$
    * 测试$X_e$是否正确的图存在`reio_mine02`

* fix the `z_start`, constrain the `r`
    * z_start=7.6711
    * r: 0.01,0.26,0.01

## 1203更新：只限制r
`reio_camb05`: 0.11
`reio_camb06`: 0.09
`reio_camb07`: 1

* 0.15,0.05 Fisher=0.0002809
* 1 Fisher=0.0002680
* 0.11,0.09 Fisher=0.0002809

* std of chi2_BB=95647.47
* std of posterior=7.57*10**(-68)

## 1205更新：试试加lensing有没有数量级变化
`reio_camb08`: 1
`reio_camb09`: lensing fid

---
试试算reio_camb的chi2
* r: 0.01,0.26,0.01

## 1206更新：步长太大
* 新步长r: 
    * r_start=0.07
    * r_end=0.1205
    * r_step=0.0005

## 1208meeting更新
* $\Delta r\sim10^{-6}$
* 调$\Delta z$
* 只用`camb` model

## 1212结果更新：
* $\Delta z$: 0.1 0.9 0.00001
* $\sigma$: 0.0014604267851034088
* fisher: 11.382641016831142
* 算fisher: 
    * 0.4: reio_camb01
    * 0.6: reio_camb00

## 1213关于`reionization_width`:
https://arxiv.org/pdf/0804.3865.pdf

$x_e(y)=\frac{f}{2}(1+\tanh(\frac{y(z_{re})-y}{\Delta_y}))$
* $y\equiv(1+z)^{3/2}$
* $z_{ze}$ measures where the reionization fraction is half of its maximum
* input is $\Delta_z$, and $\Delta_y=1.5\sqrt{1+z_{re}}\Delta_z$
* `reionization_width`就是$\Delta_z$

### 新的参数设置
* r: 0.09 0.11 0.00001
* `reionization_width`: 0.3 0.7 0.0001

## 1213关于`tau`:
* r: 0.09 0.11 0.00005
* tau_reio: 0.051 0.057 0.00001

## 1221算fisher:
* `l1p`:
    * r=0.10005
    * tau_reio=0.054
* `l1m`:
    * r=0.09995
    * tau_reio=0.054
* `l2p`:
    * r=0.1
    * tau_reio=0.0541
* `l2m`:
    * r=0.1
    * tau_reio=0.0539

* $\sigma_1$=0.00028192588780615843
* $\sigma_2$=0.00013445473900394967
* $\sigma_{12}$=-1.0662709406383502

## 1222 meeting 更新:
* 先算Fisher: +prior
    * 2D时要乘以1.5
* Fisher得到$\sigma$
    * 范围: +/- 5 $\sigma$
    * 步长: $\sigma$/10
* 算posterior时加上高斯prior
    * planck


## 1223:
* fiducial $\tau$改成了0.0561，记得改掉算fisher的值
* `l1p`:
    * r=0.10005
    * tau_reio=0.0561
* `l1m`:
    * r=0.09995
    * tau_reio=0.0561
* `l2p`:
    * r=0.1
    * tau_reio=0.0562
* `l2m`:
    * r=0.1
    * tau_reio=0.0560

## 1228:
* 只constrain r，加EE
* Fisher要更新C_l
* 需要带tCl
    * `00`: r=0.1
    * `01`: r=0.10005
    * `02`: r=0.09995

* Fisher: 0.00028208515761258944

