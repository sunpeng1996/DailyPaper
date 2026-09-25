---
title: 'PUBG Ally: A Conversational Embodied Agent as an AI Teammate'
title_zh: PUBG Ally：支持语音交互的游戏AI队友对话式具身Agent
authors:
- Beomsoo Kim
- Byeongju Kim
- Dohyun Kim
- Dongwon Kim
- Eunchong Kim
- Hongmin Kim
- Hyeojung Im
- Hyeonbin Hwang
- Hyeonghwan Kim
- Hyoseok Seol
affiliations:
- KRAFTON AI
arxiv_id: '2609.29837'
url: https://arxiv.org/abs/2609.29837
pdf_url: https://arxiv.org/pdf/2609.29837
published: '2026-09-23'
collected: '2026-09-25'
category: Agent
direction: 具身Agent · 端侧人智协同交互
tags:
- EmbodiedAgent
- ConversationalAgent
- OnDeviceDeployment
- HumanAgentCollaboration
- SLM
one_liner: 提出分层架构的对话式具身游戏Agent，支持端侧部署，可作为AI队友与人类玩家实时语音协同游玩PUBG
practical_value: '- 分层架构可直接迁移到实时交互Agent场景，如电商直播导购、智能客服：上层LLM负责意图理解、话术生成、高层决策，下层规则引擎处理低延迟高确定性动作，避免LLM进入实时控制路径，大幅降低推理成本与延迟

  - 事件驱动的推理调度+reactivity priors配置可复用在用户交互类Agent中，无需重新训练模型就能调整Agent响应频率、主动/被动交互比例，适配不同业务场景的用户预期

  - 端侧部署的上下文优化技巧可复用在端侧推荐/搜索Assistant场景：包括缓存友好的prompt布局、动态上下文压缩、过时状态自动清理，降低KV cache开销，提升推理速度

  - 用户偏好对齐的评估方法可迁移到推荐/Agent系统效果评估：不要仅依赖离线指标，结合真实用户交互反馈迭代评估标准，有效缩小离线线上效果gap'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有游戏AI大多仅侧重自主对战能力，无法同时满足快节奏场景下的低延迟操作、自然语音交互、言行同步的协同需求；而对话式具身Agent在游戏陪伴、电商直播导购、家庭服务机器人等场景具备广泛落地价值，但缺乏可规模化落地的工程架构与训练方案。
### 方法关键点
- 分层双系统架构：参考System1/System2认知框架，上层System2为事件驱动的SLM Agent，通过16个受限工具接口查询游戏状态、生成回复话术、下发高层动作指令，不直接进入实时控制链路；下层System1为行为树引擎，按游戏tick频率执行动作，处理移动、战斗、救援等低延迟操作，两层联动保证Agent言行同步。
- 训练数据迭代方案：先使用31B teacher模型与真实玩家对战，采集3.9万局真实会话数据；后续迭代时针对学生模型落地遇到的分布外场景，用teacher模型生成修正轨迹，结合DAgger思想扩充训练集，再通过「8B中间teacher SFT → 2B/1.7B小模型off-policy KD → 小模型on-policy KD」三步蒸馏得到可端侧部署的模型。
- 端侧优化技巧：通过模型压缩、动态上下文清理、缓存友好的prompt布局（稳定前缀前置，过期状态不跨轮携带）降低推理开销，配合runtime guardrails保障内容安全。
### 关键结果
端侧全链路（STT+SLM+TTS）单次交互延迟1.6s，仅为云部署方案的47%；面向141个国家的beta测试中，使用过Ally的用户推荐率正反馈比负反馈高25.1个百分点，50%的用户将Ally定位为队友/陪伴者而非工具。
### 核心洞察
实时交互类Agent落地的核心是将LLM从高频率低容错的实时控制路径中解耦，用分层架构平衡推理能力与响应延迟，同时通过真实用户交互数据迭代解决分布偏移问题。
