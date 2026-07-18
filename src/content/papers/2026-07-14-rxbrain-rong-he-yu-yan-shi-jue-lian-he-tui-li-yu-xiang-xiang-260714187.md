---
title: 'RxBrain: Embodied Cognition Foundation Model with Joint Language-Visual Reasoning
  and Imagination'
title_zh: RxBrain：融合语言视觉联合推理与想象的具身认知基础模型
authors:
- Haotian Liang
- Mingkang Chen
- Yufei Huang
- Yuchun Guo
- Xiaomeng Zhu
- Xiangli Shi
- Kaixuan Wang
- Yunxuan Mao
- Weijie Zhou
- Ling Chen
affiliations:
- Tencent Robotics X Team
- Futian Laboratory
- Tencent Hy Team
arxiv_id: '2607.14187'
url: https://arxiv.org/abs/2607.14187
pdf_url: https://arxiv.org/pdf/2607.14187
published: '2026-07-14'
collected: '2026-07-18'
category: Agent
direction: 具身Agent · 多模态联合推理规划
tags:
- Embodied AI
- Multimodal Reasoning
- Vision-Language Model
- World Model
- Robotics
one_liner: 提出基于模态感知MoT架构的具身认知基础模型，支持联合文本推理与视觉想象生成端到端具身规划
practical_value: '- 多模态架构设计可复用：MoT架构中同模态下理解与生成任务共享注意力层、仅路由到不同FFN专家的设计，可迁移至多模态生成式推荐、商品文案+商品图联合生成场景，降低多任务训练的参数量开销

  - 自动化数据标注方案可借鉴：将视频自动拆解为动作片段+对应视觉状态转换的标注流水线，可用于短视频场景下的用户行为序列建模、商品种草视频的语义-视觉对齐数据集构建，大幅降低人工标注成本

  - 交错生成范式可用于Agent决策：文本推理+视觉状态验证的迭代规划流程，可迁移至电商智能导购Agent、线下零售机器人的任务规划，通过视觉想象预演动作效果降低实际执行错误率'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有具身AI方案存在能力割裂问题：VLM类方案仅能输出纯文本推理逻辑，缺失对动作后物理状态的显式视觉想象，易忽略空间、状态等关键细节；世界模型类方案仅能做视觉状态预测，缺失抽象因果推理、约束感知能力，无法输出可解释的规划逻辑，二者分离导致生成的具身规划可执行性差，无法同时覆盖「做什么」和「做完是什么状态」的双重规划需求。
### 方法关键点
- 架构：采用模态感知Mixture-of-Transformers（MoT）统一架构，总参6.2B，语言分支、视觉理解分支各约1.5B，视觉生成专属FFN专家2.4B；视觉理解与生成任务共享ViT的QKV投影层，仅路由到不同FFN专家，兼顾跨任务特征对齐与计算效率
- 数据：自动化流水线将5万+小时具身视频拆解为4级粒度的文本-视觉对齐训练样本，覆盖单步状态转换、步骤级规划、子目标规划、终态想象，标注通过率75.18%，共获得2150万+训练片段
- 训练：两阶段训练，第一阶段用大规模图文对做预训练对齐语义空间，第二阶段用具身多模态数据微调，学习文本推理与视觉想象交错生成的规划能力
- 评估：提出RxBrain-Bench，包含EVQA（具身问答）、WorldPred（世界状态预测）、JointPlan（联合规划）三个赛道，首次完整评估多模态交错规划能力
### 关键结果
在RxBrain-Bench-EVQA赛道准确率超出同类SOTA约12%，WorldPred赛道综合得分超出Cosmos-3-Nano等基线约18%，JointPlan赛道联合规划得分超出基线22%，无需大规模动作数据预训练即可在真实机器人部署中获得可用性能。

最值得记住的结论：具身规划的核心是文本逻辑与视觉状态的互补协同，而非两种模态能力的简单叠加。
