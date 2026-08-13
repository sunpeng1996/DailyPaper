---
title: 'AtlasVLA: Persistent World-Ego State Modeling for Vision-Language-Action Models'
title_zh: AtlasVLA：面向视觉语言动作模型的持久化世界-自我状态建模
authors:
- Guiyu Zhao
- Longteng Guo
- Yanghong Mei
- Zilin Zhu
- Yu Zhang
- Bin Cao
- Mingming Yu
- Xingjian He
- Jie Jiang
- Jing Liu
affiliations:
- Institute of Automation, Chinese Academy of Sciences
- University of Chinese Academy of Sciences
- Beijing Freedo Technology Co., Ltd.
- Beihang University
arxiv_id: '2608.06729'
url: https://arxiv.org/abs/2608.06729
pdf_url: https://arxiv.org/pdf/2608.06729
published: '2026-08-06'
collected: '2026-08-13'
category: Agent
direction: 具身Agent · VLA持久化状态建模
tags:
- VLA
- Embodied Agent
- Dual Memory
- DiT
- Long-Horizon Task
one_liner: 提出带双记忆架构的AtlasVLA，解决单相机VLA的感知与任务进度遗忘问题，长时序任务性能超SOTA
practical_value: '- 双记忆架构可迁移到长交互链路电商导购Agent，持久化存储用户浏览/交互状态与任务进度，解决上下文遗忘问题

  - voxel-hashed全局状态更新方法可复用在多模态推荐的用户状态建模，压缩长序列行为特征，降低长时序推荐的遗忘率

  - DiT结合全局状态做条件生成的范式，可迁移到生成式推荐的多轮交互后个性化内容生成场景，提升生成结果匹配度'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有VLA模型为响应式范式，仅依赖瞬时输入决策，在单腕带相机、部分可观测长时序任务下，存在物体出视野后的感知遗忘、多步执行的任务进度遗忘两大瓶颈，性能受限。
### 方法关键点
1. 设计双内存架构：4D持久化世界状态内存将瞬时2D观测转换为全局更新的voxel-hashed空间状态，解决视觉盲区；自我工作状态内存追踪历史自身状态与任务进度
2. 将联合世界-自我状态作为条件输入扩散Transformer（DiT），实现鲁棒空间推理
### 关键结果
仅用单腕带相机就达到SOTA性能，显著优于多视角基线：LIBERO-Long数据集上成功率绝对提升9.4%，真实世界长时序任务成功率绝对提升17.5%
