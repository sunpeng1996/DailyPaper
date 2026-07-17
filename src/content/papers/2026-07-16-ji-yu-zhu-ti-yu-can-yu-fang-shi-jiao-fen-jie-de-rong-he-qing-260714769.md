---
title: Dialogue Summarization with Emotion Dynamics Using Topic- and Participant-Centric
  Decomposition
title_zh: 基于主题与参与方视角分解的融合情绪动态的对话摘要方法
authors:
- Linyun Xiang
- Mark Neerincx
- Stephanie Tan
affiliations:
- Delft University of Technology
arxiv_id: '2607.14769'
url: https://arxiv.org/abs/2607.14769
pdf_url: https://arxiv.org/pdf/2607.14769
published: '2026-07-16'
collected: '2026-07-17'
category: Agent
direction: Agent 分层协作对话摘要
tags:
- DialogueSummarization
- Chain-of-Agents
- EmotionModeling
- Multimodal
- TextSummarization
one_liner: 提出层级Chain-of-Agents框架，通过双视角对话分解生成融合语义与情绪轨迹的对话摘要
practical_value: '- 客服场景对话摘要可复用双视角分解思路：先按会话主题切分、再按参与方（用户/客服）分别汇总，同时保留用户情绪变化轨迹，支撑后续服务满意度预判、舆情识别

  - 分层Agent链架构可直接迁移至多轮会话处理任务：下层Agent负责细分片段的语义+情绪提取，上层Agent负责汇总生成最终结果，适配小语言模型落地，降低推理成本

  - 评估环节可复用情绪轨迹度量指标，针对会话类任务补充语义准确率之外的情感保留度评估，优化面向用户感知的下游任务效果'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有文本摘要研究多聚焦独白类内容（如新闻、报告），未考虑对话场景下多参与方交互特性，普遍缺失对情绪动态变化的建模，无法支撑对话下游的情感相关分析需求。
### 方法关键点
基于改进的层级Chain-of-Agents架构，从两个维度分解多模态对话输入：一是基于所有参与方utterance划分主题片段，二是提取每个参与方的专属话语片段。两类片段分别生成融合自动推断情绪的子摘要，再聚合为同时包含语义内容与情绪变化轨迹的最终对话摘要，同时新增情绪轨迹度量指标，用于评估摘要对情感流动的保留能力。
### 关键结果
在多模态对话数据集上基于小语言模型开展实验，生成的摘要同时具备高质量语义内容与情绪信息，显式情绪标签可用场景下方法有效性得到进一步验证。
