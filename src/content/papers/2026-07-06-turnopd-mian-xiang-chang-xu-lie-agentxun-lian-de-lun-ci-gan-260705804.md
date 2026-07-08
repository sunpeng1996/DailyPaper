---
title: 'TurnOPD: Making On-Policy Distillation Turn-Aware for Efficient Long-Horizon
  Agent Training'
title_zh: TurnOPD：面向长序列Agent训练的轮次感知高效同策略蒸馏
authors:
- Yuhang Zhou
- Kai Zheng
- Haoling Li
- Dengyun Peng
- Can Xu
- Jingjing Chen
affiliations:
- Fudan University
- Tencent Hunyuan
arxiv_id: '2607.05804'
url: https://arxiv.org/abs/2607.05804
pdf_url: https://arxiv.org/pdf/2607.05804
published: '2026-07-06'
collected: '2026-07-08'
category: Agent
direction: Agent训练优化 · 同策略蒸馏
tags:
- On-Policy Distillation
- Long-Horizon Agent
- Training Efficiency
- Knowledge Distillation
- Turn-Aware
one_liner: 提出双控制器轮次感知同策略蒸馏框架，大幅提升长序列Agent训练效率与精度
practical_value: '- 训练电商导购、多轮搜索推荐类Agent时，可直接复用自适应rollout深度控制器，动态截断低价值尾轮交互，最高可节省56%训练算力，精度损失可忽略

  - 多轮交互Agent的损失函数可引入渐进式轮次归一化混合策略，早期用token级权重保证训练稳定性，后期逐步提升轮次均衡权重，改善深层决策点训练不足问题

  - 多轮推荐Agent优化时，可参考其轮次级信号分析方法，定位损失集中的浅轮和训练不足的深轮，针对性分配计算与监督资源，降低训练成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

#### 动机
现有同策略蒸馏（OPD）是语言Agent训练的主流方案，但在长序列多轮Agent任务上存在两大核心效率瓶颈：固定全长度rollout浪费大量算力在信号弱、噪声大的尾轮；轨迹级KL损失权重集中在浅层token，深层决策轮训练严重不足，导致训练速度慢、最终精度天花板低。

#### 方法关键点
- 自适应rollout深度控制器：基于探针采集的轮次KL统计和任务成功率覆盖阈值，动态选择每轮训练的rollout长度，平衡训练效率与任务覆盖度
- 渐进式轮次归一化损失控制器：训练过程中线性调整损失权重，从初始token级加权逐步过渡到轮次均衡加权，逐步提升深层决策轮的监督权重

#### 关键结果
在ALFWorld、WebShop（电商导购场景）、多跳搜索三个长序列Agent基准上对比 vanilla OPD、TCOD-F2B基线：ALFWorld 1.7B模型相同训练步长下精度从83.0提升至86.3，训练时间从4.42h降至1.93h，提速2.29倍；WebShop场景精度提升的同时训练时间从1.57h降至1.24h；多跳搜索场景相同时间预算下精度比基线高1.47个点。

**最值得记住的一句话**：长序列Agent训练的核心监督单元不是扁平的token，而是嵌入交互轨迹的轮次级决策
