---
title: 'Demonstration of MANA: Multi-perspective Alignment of NPC Agents'
title_zh: MANA：多视角对齐的NPC智能体系统演示
authors:
- Amir Tahmasbi
- Keshav Singh
- Shaheer Raza
- Owen Mei
- Jason Wu
affiliations:
- Purdue University
arxiv_id: '2611.14431'
url: https://arxiv.org/abs/2611.14431
pdf_url: https://arxiv.org/pdf/2611.14431
published: '2026-11-10'
collected: '2026-11-12'
category: Agent
direction: 具身Agent 演示驱动的行为与 persona 对齐
tags:
- Embodied Agent
- NPC Alignment
- Programming by Demonstration
- LLM
- In-situ Learning
one_liner: 通过游戏内第一人称交互演示，快速对齐NPC的行为逻辑与persona，支持跨场景自主决策
practical_value: '- 电商导购/客服Agent可直接复用「演示+蒸馏」范式：运营无需编写prompt，仅需扮演Agent完成若干真实场景交互，LLM即可自动蒸馏得到persona与应答/动作规则，大幅降低Agent对齐成本

  - 多智能体协作场景可参考跨模态补全设计：仅通过行为演示即可自动生成匹配的语言输出，无需分别标注动作与对话数据，降低多模态Agent的训练标注成本

  - 推荐系统的用户/物品画像建模可复用行为蒸馏逻辑：从用户交互序列中自动蒸馏出可解释的偏好规则+persona描述，可直接用于提升召回排序的可解释性与个性化匹配精度'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
传统游戏NPC行为依赖人工编写行为树、目标规划逻辑，难以覆盖全场景分支；现有LLM驱动的智能NPC需要开发者反复调试prompt，非AI专业从业者对齐成本极高；此前的演示式NPC对齐方案需要单独构造训练场景，泛化性弱，难以迁移到未见过的新场景。
### 方法关键点
- 三阶段Pipeline：演示阶段开发者可随时接管任意NPC的第一人称视角，同步记录两类数据：交互对话流、每固定tick的<动作-环境上下文>对（包含周边实体的类型、距离、方向等信息）
- 蒸馏逻辑：LLM自动从演示数据中提炼双组件行为画像：自然语言格式的persona（包含性格、语气、核心偏好），以及可解释的动作政策（包含空间、时序、优先级规则，明确不同场景下的动作选择逻辑）
- 部署逻辑：运行时NPC实时感知当前环境与上下文，输入画像条件化的政策，自主生成动作与对应对话，无需额外prompt工程
### 关键结果
在Minecraft环境测试，仅需约2分钟的游戏内演示即可完成单NPC对齐，生成的NPC在未见过的战斗、社交场景下行为一致性达100%，完全符合演示设定的persona（如攻击性猎人主动攻击怪物、胆小农民夜间主动躲进避难所）；即使演示阶段未提供任何对话数据，NPC也能自主生成与行为匹配的对话内容，跨模态补全效果达标。
### 核心洞见
对非AI专业的开发者/运营而言，「直接演示预期行为」比「撰写prompt描述预期行为」的成本低得多，且对齐效果更可控。
