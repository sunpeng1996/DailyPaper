---
title: 'The Precision Wall: An Optimizer-Dependent Boundary for Optimization under
  Power-Law Measurement Spectra'
title_zh: 《精度墙：幂律测量谱下依赖优化器的优化边界
authors:
- Lngel Kyo
affiliations:
- A2O Labs
arxiv_id: '2610.40485'
url: https://arxiv.org/abs/2610.40485
pdf_url: https://arxiv.org/pdf/2610.40485
published: '2026-10-29'
collected: '2026-11-01'
category: Training
direction: 低秩矩阵恢复 · 优化器精度边界分析
tags:
- Optimizer
- Low-Rank Recovery
- Adam
- Power-law Spectrum
- Hessian
one_liner: 推导幂律测量谱下优化器依赖的精度边界公式，可准确预测Adam优化的停滞阈值
practical_value: '- 电商推荐低秩矩阵补全场景，可参考本文公式预判Adam收敛上限，通过调整隐向量维度D缓解长尾数据训练停滞问题

  - 低秩建模训练时，当监控到Hessian最小特征值低于1e-8时可提前终止训练，节省冗余算力消耗

  - 长尾稀疏数据训练时，可参考优化器分母精度阈值调整Adam正则项，避免长尾方向梯度被归一化噪声淹没'
score: 4
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有低秩矩阵恢复的非凸优化收敛性保证均基于各向同性测量假设，而电商用户-物品交互、自然语言词频等真实数据的协方差谱均服从幂律分布，一阶优化器在幂律指数过高时会意外停滞，现有理论无法解释该现象。
### 方法关键点
1. 定位停滞根源为精度墙：真值处非规范Hessian最小特征值领先阶缩放为$V^{-(s+1)}D^{-s}$，当曲率低于优化器有效分母下限$\epsilon_O$时，归一化噪声会淹没长尾方向梯度
2. 推导优化器相关的临界幂律指数公式，包含优化器精度项与检测滞后项两个核心参数
3. 可区分分母精度墙、条件数墙、符号量化墙三类优化停滞原因
### 关键结果
校准Adam滞后项后，公式在16组$V\in\{64,128,256,512\}$、$D\in\{4,8,16,32\}$的验证集上预测Adam停滞阈值误差≤0.45；公式在D=2时失效，精度下限饱和于$10^{-8}$动态阈值
