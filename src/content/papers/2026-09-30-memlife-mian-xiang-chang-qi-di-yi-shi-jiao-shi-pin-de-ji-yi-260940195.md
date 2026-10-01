---
title: 'MemLife: Curating and Reasoning over Long-Term Egocentric Video Memories'
title_zh: MemLife：面向长期第一视角视频的记忆构建与推理系统
authors:
- Guangzhi Xiong
- Xinyuan Zhang
- Xiao Yang
- Hyokun Yun
- Kai Zhang
- Shiun-Zu Kuo
- Hyeonjeong Ha
- Xilun Chen
- Kai Sun
- Lucas Liang
affiliations:
- Meta Reality Labs
- University of Virginia
- University of Illinois Urbana-Champaign
arxiv_id: '2609.40195'
url: https://arxiv.org/abs/2609.40195
pdf_url: https://arxiv.org/pdf/2609.40195
published: '2026-09-30'
collected: '2026-10-01'
category: Agent
direction: Agent 长时序多模态记忆优化
tags:
- Long-term Memory
- Egocentric Video
- Multimodal Agent
- RAG
- Reinforcement Learning
one_liner: 提出实体锚定第一人称的视频记忆系统MemLife及RL优化框架MemOpt，长时序视频QA精度领先基线最高12%
practical_value: '- 个人化Agent/导购助手的记忆模块可直接复用「实体锚定+第一人称叙述」的写入设计，对齐用户日常query的表述习惯，大幅降低语义检索的匹配gap

  - 长序列RAG系统的记忆生成优化可复用FIRM奖励框架，仅优化写入环节，从忠实度、信息密度、可检索性三个维度做RL训练，避免端到端训练的读取侧噪声

  - 电商用户长周期行为历史召回场景，可加时间索引+检索结果按时间序排序的设计，既缩小检索范围又提升下游LLM推理的准确率'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
长期第一视角视频可支撑个人AI助理回答用户过往生活相关问题，但随着视频时长累计到数百小时级，逐query重处理原始视频的算力成本不可接受。现有将视频压缩为文本记忆的方案普遍存在两类问题：要么压缩强度过高丢失关键证据，要么保留过多冗余信息导致检索竞争加剧召回失败，同时写入幻觉还会引入错误证据，无法满足实用要求。
### 方法关键点
- **MemLife系统**：写入端采用多模态融合+实体锚定+第一人称叙述的设计，将30s视频片段转化为带时间戳的结构化文本记忆，片段间无依赖，计算与存储成本随时长线性增长；读取端为Agentic检索器，支持query改写、时间范围过滤、证据按时间序返回，可选调用原始视频帧工具补全视觉细节
- **MemOpt优化框架**：仅优化记忆写入器，固定读取端避免训练噪声，采用FIRM三维奖励：token级忠实度（惩罚与视频源不符的内容）、信息度（奖励保留问答关键事实的内容）、可检索性（奖励易被召回的表述），通过GRPO算法优化
### 关键实验结果
在SuperMemory-VQA、EgoLifeQA等4个长时序视频QA基准上，零训练的MemLife比最优无训练基线精度高4.6~12.0%；叠加MemOpt优化后精度再提升2.7~5.0%，整体比现有SOTA系统高4.0~17.0%，记忆体积最多压缩31倍，优化后的写入器可跨模型、跨记忆系统迁移。
### 最值得记住的结论
学习「该记住什么」是长时序记忆QA的核心优化杠杆，仅优化记忆写入器的收益远高于优化检索推理逻辑，且泛化性更强
