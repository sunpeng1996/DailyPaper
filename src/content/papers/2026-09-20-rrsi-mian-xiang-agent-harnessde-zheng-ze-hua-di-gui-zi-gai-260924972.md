---
title: 'RRSI: Regularized Recursive Self-Improvement of Agent Harnesses'
title_zh: RRSI：面向Agent Harness的正则化递归自改进框架
authors:
- Peng Xia
- Rujun Han
- Zifeng Wang
- Yanfei Chen
- Yufan Zhang
- Yoonho Lee
- Chengsong Huang
- Han Yu
- Zhongying CuiZhu
- Yifei Ming
affiliations:
- Google Cloud AI Research
- UNC-Chapel Hill
- Stanford University
- Washington University in St. Louis
arxiv_id: '2609.24972'
url: https://arxiv.org/abs/2609.24972
pdf_url: https://arxiv.org/pdf/2609.24972
published: '2026-09-20'
collected: '2026-09-22'
category: Agent
direction: Agent系统优化 · Harness自进化
tags:
- Agent
- RSI
- Harness Evolution
- Regularization
- Generalization
one_liner: 提出双端正则约束的Agent Harness递归自改进框架，解决进化集过拟合、跨任务泛化差问题
practical_value: '- 电商导购/客服/选品Agent的Harness迭代可直接复用双端正则逻辑：提议端加退火稀疏更新约束，避免一次修改过多导致不可归因，降低无效迭代成本

  - Harness验收环节新增三层过滤规则：先筛掉场景特化硬编码逻辑，再设噪声阈值过滤随机波动假收益，最后要求新增token消耗匹配效果增益，避免越迭代推理成本越高

  - 自进化推荐系统的prompt/工具链迭代可引入历史轨迹归因机制，记录每次修改的收益/成本，迭代卡住时主动切换到未探索组件，跳出局部最优

  - 跨模型迭代时无需为每个LLM重写Harness，RRSI进化出的通用Harness可直接适配不同大小的模型，小模型也能获得明显收益，降低模型迭代的适配成本'
score: 9
source: huggingface-daily
depth: full_pdf
---

### 动机
当前Agent性能很大程度由Harness（prompt、控制流、工具、内存、上下文管理）决定，现有自动Harness进化方法容易过拟合训练任务，分布内收益高但分布外收益大幅缩水甚至消失，同时进化出的Harness冗余度高、推理token消耗大，难以落地到实际业务。

### 方法关键点
- 提议端正则：①退火更新稀疏度：每轮允许的修改条数随迭代轮次余弦退火下降，早期允许大范围探索，后期要求稀疏可归因修改；②证据感知归因：记录所有历史修改的效果、成本、接受状态，避免重复测试已被证伪的方案；③结构化探索：迭代停滞时强制分配预算到未探索的Harness组件，跳出局部最优
- 选择端正则：①泄漏筛查：提前过滤含进化集特化逻辑（如任务名、固定答案）的修改；②稳定性验收：基于基础Harness的实测噪声阈值，拒绝收益低于噪声的修改；③复杂度感知验收：新增token消耗必须和效果增益正相关，避免无意义的成本上升；④结构剪枝：定期删除长期无正向贡献的Harness组件，保持精简

### 关键实验
在编码、Agent工作空间、工程设计3个领域共8个benchmark测试，对比Meta-Harness、AHE等4个SOTA基线：①进化集最高增益14.1分，5个分布外基准最高增益4.7分，相对基线OOD平均性能最高提升22.9%；②进化出的Harness比无正则进化版本少消耗30%的policy token；③进化出的Harness可直接跨模型迁移，给未参与进化的小模型带来30.4%的相对性能提升。

### 核心结论
Agent自进化过程中，控制修改的规则比开放修改的空间更重要，正则化迭代动态比单纯追求进化集收益更能带来可落地的通用能力。
