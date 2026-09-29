---
title: 'Beyond Dyadic Memory: Interaction-Aware Multimodal Memory with Adaptive Agentic
  Retrieval for Multi-Party Spoken Conversations'
title_zh: 面向多方语音对话的交互感知多模态记忆与自适应智能检索
authors:
- Wenxu Jia
- Xize Cheng
- Zihan Zhang
- Dongjie Fu
- Linjun Li
- Wenshi Chen
- Yangyang Wu
- Tao Jin
affiliations:
- Zhejiang University
- Meituan
arxiv_id: '2609.32522'
url: https://arxiv.org/abs/2609.32522
pdf_url: https://arxiv.org/pdf/2609.32522
published: '2026-09-26'
collected: '2026-09-29'
category: Agent
direction: Agent 多模态长时记忆与检索优化
tags:
- Conversational Agent
- Multimodal Memory
- GRPO
- Speaker Identification
- Adaptive Retrieval
one_liner: 提出VoxPolyMem多模态记忆框架，适配多方语音对话，性能超现有最强基线23.6分
practical_value: '- 多角色交互场景（如直播导购、商家客服群、会议助手）可复用三层记忆架构：交互记忆存原始会话与有向交互关系、事实记忆存结构化信息、画像层存参与者偏好，提升跨会话信息召回准确率

  - 自适应检索的EG-GRPO奖励机制可迁移到各类RAG系统，按轮次仅对新获取的有效证据加权分配奖励，减少无效检索轮次，降低推理延迟

  - 增量声纹匹配+会话后身份合并方案可直接用于语音交互产品（如智能客服、车载助手），无需预定义用户数量即可识别跨会话重复参与者，降低冷启动成本'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有Agent长时记忆方案大多聚焦二元文本/图文对话，未覆盖多方语音对话场景：该场景需跨会话识别说话人、存储交互关系（谁说了什么给谁），固定检索策略易漏检跨层跨模态信息，传统终端奖励无法区分每轮检索的实际贡献，导致召回效率低、个性化回答准确率差。
### 方法关键点
- 增量说话人识别：用ECAPA-TDNN提取声纹embedding，增量匹配+EMA更新声纹库，会话后自动合并碎片化ID，无需预定义参与者数量
- 三层交互感知记忆架构：交互记忆存储原始多模态会话与有向交互图（记录说话人、收话人），事实记忆存储结构化对话事实，用户画像存储身份、声纹、偏好，三类记忆分别独立建索引
- 自适应智能体检索：检索Agent根据已有证据动态选择记忆层、检索工具、改写查询；提出EG-GRPO训练策略，每轮仅对新获取的有效证据加权奖励，鼓励互补检索，避免重复召回
### 关键实验结果
构造VoxPolyBench多方语音对话记忆基准，含18个场景、176个会话、18.9小时合成语音、1527条QA；VoxPolyMem在该基准得分85.0，超最强基线23.6分；在公开Mem-Gallery、H2HMem-Multi基准上分别得分89.6、74.4，超最强基线11.8、8.4分；EG-GRPO可将平均检索轮次从1.6降至1.2，同时提升证据召回率。
### 核心结论
多角色交互场景下，显式存储交互关系而非仅存储会话内容，配合按证据增益分配奖励的检索策略，可大幅提升长时记忆的利用效率。
