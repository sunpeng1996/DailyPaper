---
title: 'ToolArtist: Tool-Using Unified Multimodal Models for Agentic Image Generation'
title_zh: ToolArtist：支持工具调用的统一多模态智能体图像生成模型
authors:
- Jiahao Zhao
- Xiaomin Yu
- Zhongxiang Sun
- Fengwei Teng
- Chengwei Qin
- Xiaobin Hu
- Jun Xu
- Shuicheng Yan
affiliations:
- RUC
- HKUST(GZ)
- NUS
- UCD
arxiv_id: '2608.04436'
url: https://arxiv.org/abs/2608.04436
pdf_url: https://arxiv.org/pdf/2608.04436
published: '2026-08-04'
collected: '2026-08-06'
category: Agent
direction: 多模态智能体 · 工具调用图像生成
tags:
- Tool-using Agent
- Multimodal LLM
- Image Generation
- SFT
- RL
- GRPO
one_liner: 通过两阶段后训练将推理、工具调用、原生生图统一为单一多模态智能体策略，提升开放域生图事实准确性
practical_value: '- 电商营销素材/商品图生成场景可复用「文本+图像搜索先验增强」思路：生成特定文化、地域、IP相关素材时，先检索事实信息和参考图再生成，避免常识错误。

  - 两阶段后训练策略可直接迁移至多模态智能体落地：SFT阶段用教师智能体生成全链路轨迹，再转换为基础模型原生输出格式，无需改动底座架构即可注入工具调用+生成的联动能力，降低改造门槛。

  - RAD-GRPO双奖励设计可复用：生成类智能体优化时，同时奖励「生成意图准确性」和「最终输出质量」，比仅看最终输出的奖励信号更稳定，可避免智能体仅调用工具不输出、生成内容偏离意图的问题。

  - 图像搜索结果附源网页语义摘要的trick，可大幅提升参考图引用的语义准确性，避免选到视觉相似但事实错误的参考，适合对商品细节、IP还原度要求高的生图场景。'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有文本生成图像模型在需复杂语义理解、多步推理、外部知识支撑的开放域任务中，容易生成视觉合理但事实错误的结果；现有带智能体能力的生图方案要么采用固定工作流，要么仅部分环节由智能体控制，推理、工具调用、生图没有统一策略调度，效果上限低。

### 方法关键点
- 基于统一多模态模型（UMM）Emu3.5做两阶段后训练得到ToolArtist，将推理、文本/图像搜索工具调用、原生生图整合为单一智能体策略，无需预设流程，由模型自主决策动作顺序和终止条件。
- SFT阶段：用教师智能体生成包含推理、工具调用、外部生图的完整轨迹，再将外部生图环节转换为模型原生的视觉描述+视觉token格式，仅用7132条高质量轨迹即可注入基础能力。
- RL阶段：提出RAD-GRPO算法，用双奖励（意图奖励评估生成描述的准确性、质量奖励评估最终生图的保真度与美观度）+ 辅助奖励（格式校验、生成触发、长度惩罚等）联合优化全链路策略。

### 关键实验
在WISE（1000条覆盖文化、时空、自然科学的开放域生图prompt）数据集上Overall得分0.79，超过现有开源智能体生图方案；在WorldGenBench-Humanities（732条人文知识类生图prompt）上平均KCS得分22.10，为非专有模型最优，比次好开源方案高0.34。

### 核心结论
将图像生成作为智能体的自主决策动作而非固定流程下游环节，是提升开放域生成任务事实性的核心。
