---
title: 'EvoReason: Self-Evolving Reasoning Primitive-Guided On-Policy Distillation
  for Latent Reasoning in Generative Recommendation'
title_zh: EvoReason：自进化推理原语引导的生成式推荐隐式推理蒸馏方法
authors:
- Zhuang Zhuang
- Zhipeng Wei
- Rongfeng Guo
- Shijie Li
- Peng Zhao
- Jie Chen
- Fei Pan
affiliations:
- Kuaishou Technology
- Shenzhen University
arxiv_id: '2607.29010'
url: https://arxiv.org/abs/2607.29010
pdf_url: https://arxiv.org/pdf/2607.29010
published: '2026-07-31'
collected: '2026-08-03'
category: GenRec
direction: 生成式推荐 · 隐式推理蒸馏
tags:
- Generative Recommendation
- Latent Reasoning
- On-Policy Distillation
- Semantic ID
- Chain-of-Thought
one_liner: 提出自进化推理原语+同策略蒸馏框架，将显式推理能力高效迁移到生成式推荐隐式模块，无推理链延迟
practical_value: '- 可复用推理原语构建方案：从高质量Agent推荐轨迹中抽取结构化、函数式推理原语作为伪工具，大幅降低CoT冗余，提升蒸馏效率，适合生成式推荐的CoT蒸馏场景

  - 自进化On-Policy蒸馏工程框架：教师学生共享backbone，通过置信度门控过滤低质量教师信号，叠加KV对齐损失将显式推理能力迁移到隐式token，推理阶段无需生成CoT，延迟仅比传统生成式推荐高5%左右，可直接落地生产

  - 冷启优化方案：隐式推理蒸馏对少行为用户的偏好建模增益更显著，EvoReason在冷启用户组Recall@5相对提升26%+，可直接复用解决电商/广告推荐的新用户冷启问题'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有生成式推荐的隐式推理方案大多直接蒸馏原始CoT轨迹，存在三个核心问题：一是CoT中推理模式和冗余表达纠缠，迁移效率低；二是静态离线CoT和学生训练过程的推理能力不匹配，监督信号有效性差；三是无约束CoT生成轨迹一致性低，难以学习可迁移的推理能力，导致隐式推理效果不及显式推理，无法兼顾效果和低延迟部署要求。

### 方法关键点
- 推理原语抽取：从ReAct风格的Agent推荐轨迹中抽象可复用的推理原语（如偏好提取、冲突检测），构建可动态更新的原语库，作为伪工具引导教师生成结构化低冗余CoT
- 自进化同策略蒸馏闭环：教师基于当前学生的隐式推理状态生成适配的CoT监督信号，学生训练后的推理行为反哺原语库更新，实现监督信号和学生能力的协同进化
- 混合优化目标：结合GRPO风格的outcome驱动RL损失、置信度门控OPD蒸馏损失、KV对齐损失，同时优化推荐效果和推理能力迁移效率，推理阶段仅执行隐式推理无需生成CoT

### 关键实验
在Amazon Beauty、Sports两个公开基准+快手工业广告数据集上对比SASRec、LASAR、OneRec-Think等12个SOTA baseline：公开数据集上Recall@5相对提升17%-17.9%、NDCG@5相对提升16.4%-27.4%；工业广告召回场景在线A/B测试，ADVV提升8.11%、平台收入提升6.23%；推理单样本耗时仅0.56s，和传统生成式推荐相当，仅为显式CoT推理的1/12。

### 最值得记住的一句话
生成式推荐的隐式推理蒸馏不需要依赖固定静态CoT，通过结构化推理原语+自进化同策略蒸馏的闭环，既能获得显式推理的效果增益，又能满足低延迟的线上部署要求。
