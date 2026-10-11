---
title: 'From Expression to Reaction: Role-aware Visual Transfer and Stimulus-guided
  Reasoning for Interlocutor Emotion Recognition'
title_zh: 面向对话者情绪识别的角色感知视觉迁移与刺激引导推理框架
authors:
- Wei Wang
- Zhaowu Li
- Jianjie Luo
- Fu Lee Wang
- Lap-Kei Lee
- Zhenguo Yang
affiliations:
- Guangdong University of Technology
- Hong Kong Metropolitan University
arxiv_id: '2610.03016'
url: https://arxiv.org/abs/2610.03016
pdf_url: https://arxiv.org/pdf/2610.03016
published: '2026-10-02'
collected: '2026-10-11'
category: Multimodal
direction: 多模态情绪识别 · 跨角色知识迁移
tags:
- Multimodal Recognition
- Pseudo-labeling
- Knowledge Transfer
- Context Reasoning
- Low-resource Learning
one_liner: 提出RASG双模块框架解决听众情绪识别标注不足与歧义问题，性能较基线提升超17%
practical_value: '- 低资源场景伪标签生成：可复用RVT模块高置信度样本筛选逻辑，解决电商直播/客服场景下用户反应标注不足问题

  - 多模态歧义消解：视觉模型置信度不足时触发语言模型结合上下文推理，可迁移到直播互动、智能客服的用户情绪判断场景

  - 跨角色知识迁移：从有标注的说话人数据迁移知识到无标注的听众侧，可复用在多角色互动场景的用户行为建模任务'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
对话场景下听众情绪识别存在两大瓶颈：一是听众侧标注数据稀缺导致监督不匹配，二是视觉相似的听众反应需结合说话人上下文才能消解歧义，现有方案效果受限。
### 方法关键点
提出RASG双模块框架：
1. Role-aware Visual Transfer (RVT)模块：筛选面部表情与情绪标签匹配的说话人样本，过滤听众轨迹生成高置信度伪标签，训练听众专属视觉专家，解决标注不足问题
2. Stimulus-guided Boundary Reasoning (SBR)模块：仅当视觉模型输出置信度低于阈值时触发二分类语言推理器，将说话人音频、文本作为上下文而非直接情绪证据，区分相似听众反应
### 关键结果
在MER-Cross数据集上准确率达76.25%，较基线性能提升超17%，获ACM MM 2026 MER挑战赛Track1第二名
