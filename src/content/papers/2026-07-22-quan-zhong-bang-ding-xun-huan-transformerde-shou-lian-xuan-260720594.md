---
title: When Does Recurrence Become an Algorithm? Convergence Selection in Weight-Tied
  Looped Transformers
title_zh: 权重绑定循环Transformer的收敛选择与算法实现机制
authors:
- Tong Zhang
- Junhao Hu
- Yun Peng
- Tao Xie
affiliations:
- Fudan University
- Peking University
arxiv_id: '2607.20594'
url: https://arxiv.org/abs/2607.20594
pdf_url: https://arxiv.org/pdf/2607.20594
published: '2026-07-22'
collected: '2026-07-25'
category: Training
direction: 循环Transformer · 训练机制与度量优化
tags:
- Looped-Transformer
- Weight-Tying
- Training-Mechanism
- Convergence-Metric
- Length-Generalization
one_liner: 揭示权重绑定循环Transformer的计算边界规律，提出收敛时间度量解决传统尾部指标失效问题
practical_value: '- 搭建小参数循环Transformer做搜索/推荐的长序列用户行为建模、多轮推理排序时，可遵循预算定律v≈n_tr/T_tr调整训练时的循环次数，按需控制推理速度，平衡效果和耗时

  - 评估多轮Agent、循环推理模型的有效计算量时，可复用收敛时间τ度量，替代传统的skip测试、跨步骤相似度等尾部指标，避免误判模型实际推理能力

  - 训练长序列、高复杂度任务（比如用户多步意图理解、长序列商品关联建模）时，可采用算子优先课程学习，先学好基础运算规则再做长序列拼接，解决训练死锁问题

  - 测试时循环次数可按T≈n/v动态设置，既避免计算浪费，又能解决固定循环次数下尾部位置/行为的效果衰减问题，提升长序列建模的尾序准确率'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

### 动机
现有循环Transformer的机制评估依赖尾部指标（跳过循环测试、跨步骤相似度等），但模型收敛到不动点后这些指标会完全饱和，无法区分模型是前几步完成计算后闲置，还是每轮都在执行有效计算，导致无法准确判断循环结构的实际算法逻辑，也难以优化训练和推理配置。

### 方法关键点
- 提出收敛时间τ(n,i)头部度量：统计每个位置i的解码输出首次达到最终值的循环步数，通过τ的缩放模式（常数/log/线性）识别计算机制
- 基于群词任务构建基准，覆盖不同复杂度的序列计算任务，对比权重绑定/非绑定、不同循环调度、训练课程的效果
- 用激活补丁法验证计算边界的因果性，定位循环中有效计算的位置和步骤

### 关键结果
- 预算定律：自由训练下模型每轮处理位置数v≈训练序列长度n_tr/训练循环次数T_tr，R²=0.99，T_tr=n_tr时v精确为1.0；测试时增加循环次数可将固定长度输入的尾部位置准确率从接近0提升至近100%
- 传统尾部指标与OOD泛化相关系数|ρ|≤0.32，无预测能力；τ相关头部指标预测OOD泛化的AUROC最高达1.00
- 算子优先课程学习可100%破解S5任务的训练死锁，传统长度课程成功率为0
- 在公开easy-to-hard基准上，符合预算定律的模型实现4倍长度外推，精确匹配准确率近100%

最值得记住的一句话：权重绑定循环Transformer的有效计算发生在轨迹头部，训练时循环次数与序列长度的比例直接决定推理速度，传统尾部评估指标完全无法反映其真实计算能力。
