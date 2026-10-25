---
title: Phase Transition from Random Features to Fully Trainable Networks
title_zh: 随机特征到全可训练网络的相变效应量化研究
authors:
- Xin He
- Huan Lao
- Xiliang Lu
- Shijun Zhang
arxiv_id: '2610.31663'
url: https://arxiv.org/abs/2610.31663
pdf_url: https://arxiv.org/pdf/2610.31663
published: '2026-10-22'
collected: '2026-10-25'
category: Training
direction: 神经网络训练 · 近似边界量化
tags:
- Neural Network Training
- Approximation Bound
- Phase Transition
- Random Features
- Partial Fine-tuning
one_liner: 量化部分可训练神经网络的近似边界相变规律，证实少量可训练参数即可达到接近全训的近似效果
practical_value: '- 推荐模型微调时可参考该相变规律，仅调整小比例参数即可获得接近全量微调的效果，大幅降低训练算力与时间开销

  - 初始化偏差较大的跨域迁移推荐模型，可先适当提高可训练参数比例越过相变拐点，再冻结参数压缩推理成本

  - 多场景通用推荐模型可固定下层通用特征提取层，仅微调上层<10%的参数，平衡跨场景适配效果与训练效率'
score: 4
source: arxiv-cs.LG
depth: abstract
---

### 动机
部分可训练神经网络作为固定随机特征与全可训练表示的中间方案，长期缺乏近似能力与可训练参数比例的量化关系，无法指导实际训练的参数配置优化。
### 方法关键点
在多项式谱衰减（指数α>1）与杠杆兼容性假设下，推导宽度为m、可训练比例为P的两层网络L2平方近似率边界，引入κ_P量化固定/可训练参数组相对于目标RKHS的采样失配程度，验证球面偏置ReLU特征下的理论假设，扩展分析多层网络的训练误差行为。
### 关键结果数字
d=5、初始化尺度τ=10时，仅4.1%的可训练参数即可捕获P=0到P=1近似边界下降收益的90%；15层以内的多层网络训练误差均符合该相变规律，初始化失配越大相变拐点越陡峭。
