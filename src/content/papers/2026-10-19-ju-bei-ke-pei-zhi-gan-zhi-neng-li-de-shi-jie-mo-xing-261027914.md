---
title: World Models with Configurable Perception
title_zh: 具备可配置感知能力的世界模型
authors:
- Yijun Shen
- Delong Chen
- Xianming Hu
- Kai Zhang
- Pascale Fung
affiliations:
- East China Normal University
- HKUST
arxiv_id: '2610.27914'
url: https://arxiv.org/abs/2610.27914
pdf_url: https://arxiv.org/pdf/2610.27914
published: '2026-10-19'
collected: '2026-10-22'
category: Agent
direction: Agent 世界模型可配置感知优化
tags:
- World Model
- Configurable Perception
- Task Conditioning
- Robust Planning
- Noisy Environment
one_liner: 用任务指令配置感知过滤干扰，世界模型在动态噪声环境下规划成功率平均提升22.3%
practical_value: '- 多任务推荐/搜索场景可复用任务条件编码思路：用用户实时query/场景标签作为控制信号，引导特征编码器过滤无关物品特征，降低海量候选集下的噪声干扰，提升召回排序准确率

  - 低成本数据增强方案：无需修改底层任务逻辑，仅在观测层插入任务无关干扰样本构造训练对，即可训练鲁棒编码器，适配电商/广告场景的海量无标注数据

  - 中间效果预判方法：可复用物理量探测、干扰-干净样本检索指标，提前预判下游任务表现，减少全链路AB实验成本，加速算法迭代'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
真实环境观测天然包含大量噪声与任务无关信息，现有世界模型的编码器多为任务无关设计，无法根据不同任务需求选择性过滤干扰信息，在动态干扰场景下规划成功率会出现断崖式下降，难以落地到复杂真实场景（如电商用户浏览场景下的无关商品干扰、机器人真实操作场景的无关物体干扰等）。
### 方法关键点
- 提出ConfigWM两阶段训练架构：先训练可配置编码器，再基于冻结的编码器训练动作条件动力学模型
- 可配置编码器以DINOv2为视觉backbone，Llama 3 Transformer层为预测器，输入带干扰的视觉观测、任务文本query，输出与干净目标观测对齐的任务相关特征，用InfoNCE损失优化
- 动力学模型采用因果Transformer，在任务专属的状态空间学习动作对应的状态转移规则，结合SIGReg正则化提升训练稳定性
- 规划阶段采用交叉熵方法（CEM）在任务相关隐空间做动作序列优化，直接用隐空间特征距离衡量目标达成度
### 关键实验
在Two-Room（2D导航）、Push-T（平面操作）、OGBench-Cube（3D机械臂操作）三个基准环境，动态添加0-8个与目标外观相似的独立移动干扰物，对比LeWM、Sub-JEPA、DINOv2-WM等6个主流基线：平均规划成功率优于最优基线22.3%；干扰强度最高的d8场景下仍保留83.8%的无干扰场景性能（基线仅保留42.0%）；物理量探测皮尔逊相关系数较基线平均高0.365，干扰-干净样本Top-1检索准确率提升75.5%。
### 核心结论
仅靠训练时暴露在干扰样本下不足以提升模型鲁棒性，用任务信号主动配置感知、过滤无关信息才是复杂干扰场景下的核心解法
