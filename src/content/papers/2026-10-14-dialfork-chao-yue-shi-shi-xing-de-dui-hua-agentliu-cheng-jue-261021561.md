---
title: 'DialFork: Going Beyond Factuality to Evaluate Procedural Hallucination in
  Conversational Agents'
title_zh: DialFork：超越事实性的对话Agent流程幻觉评估基准
authors:
- Sergio Burdisso
- Esaú Villatoro-Tello
- Dairazalia Sánchez-Cortés
- Yanis Labrak
- Jordi Luque
- Milos Cernak
- Petr Motlicek
affiliations:
- Idiap Research Institute
- Logitech
- Telefónica Innovación Digital
- Brno University of Technology
arxiv_id: '2610.21561'
url: https://arxiv.org/abs/2610.21561
pdf_url: https://arxiv.org/pdf/2610.21561
published: '2026-10-14'
collected: '2026-10-27'
category: Agent
direction: Agent评测 · 流程幻觉检测
tags:
- Conversational Agent
- Procedural Hallucination
- Evaluation Benchmark
- Dialogue Metric
- Guardrail
one_liner: 首个针对对话Agent流程幻觉的开源基准，配套3粒度评测任务与流程感知度量
practical_value: '- 电商客服、售后引导、售前咨询等任务型对话Agent场景，可直接复用4类流程幻觉分类做bad case标注体系，快速定位Agent流程错误根因，优化prompt或流程控制逻辑

  - Agent上线前的效果评估可复用FLOWSCORE指标，相比传统语义相似度指标，能更精准识别语义正确但流程走偏的bad case，避免漏判

  - 实时对话护栏可借鉴基于N-gram+turn embedding的流式检测方案，仅需历史合规对话样本即可训练，无需人工标注流程节点，落地成本低，平均可在2轮内检测到流程偏离'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前LLM对话Agent的幻觉评估体系仅聚焦事实错误，完全忽略了一类隐蔽且高频的故障：流程幻觉——Agent单轮回复流畅、事实正确，但整体偏离预设交互流程（如电商客服漏核用户订单信息、售后引导跳步、引导到无关任务），直接导致任务失败，现有工具完全无法检测这类问题。
### 方法关键点
- 定义4类流程幻觉：工作流匹配错误、步骤选择错误、目标替换、约束冲突，覆盖绝大多数真实场景的流程故障
- 构建DialFork基准：基于24个任务12个领域的对话模板，通过控制对话分叉点注入指定类型幻觉，生成36278条标注对话，人工验证标注一致性达91%
- 设计3粒度评测任务：集级Agent流程偏移监控、单条对话流程相似度检索、实时幻觉触发点检测
- 提出流程感知度量：FLOWKL（集级距离）、FLOWSCORE（对话级相似度），无需依赖人工标注的流程节点即可计算
### 关键结果
在7种主流embedding、5款开源大模型上的对比实验显示：FLOWSCORE在对话级流程排序任务上Kendall τ最高达0.845，比语义相似度指标平均提升22%；流式幻觉检测方案可实现1.94轮的平均定位误差，误报率仅12%。
### 核心结论
对话的流程相似度与语义相似度是完全独立的两个维度，语义完全正确的对话也可能存在严重的流程偏离。
