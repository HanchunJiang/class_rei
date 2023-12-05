# 计算$\chi^2$
* 算正确的$C_l$
    * 用`reio_camb`
    * 结果存在`reio_camb04`
* 算错误的$C_l$
    * 测试$X_e$是否正确的图存在`reio_mine02`

* fix the `z_start`, constrain the `r`
    * z_start=7.6711
    * r: 0.01,0.25,0.01

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
* r: 0.01,0.25,0.01