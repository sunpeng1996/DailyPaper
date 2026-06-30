---
title: Multi-Agentic System Leveraging Open-Source LLMs to Mitigate Disinformation
  Threats
title_zh: 基于开源LLM的多智能体系统缓解虚假信息威胁
authors:
- Sebastian Kula
- Martin Tamajka
affiliations:
- Kempelen Institute of Intelligent Technologies
- West Pomeranian University of Technology in Szczecin
arxiv_id: '2606.30259'
url: https://arxiv.org/abs/2606.30259
pdf_url: https://arxiv.org/pdf/2606.30259
published: '2026-06-29'
collected: '2026-06-30'
category: MultiAgent
direction: 多智能体协作 · 开源LLM虚假信息检测
tags:
- MultiAgent
- Open LLM
- LLM
- Consensus Mechanism
- Disinformation Detection
one_liner: 模拟人类标注员行为构建多智能体，虚假信息检测效果优于单个LLM含GPT-4
practical_value: '- 模拟人类群体决策的多智能体共识机制，可复用在电商内容审核、虚假广告识别等需多维度校验的业务场景

  - 认知多样性+知识多样性+分层结构的设计思路，可优化推荐系统的内容风控、事实类搜索结果校验

  - 异构开源LLM组合方案透明可控，适合合规要求高的内容审核类业务落地'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
虚假信息借助社交平台和AI快速扩散，整体规模远超出人工事实核查的处理能力，单一大语言模型检测虚假信息的效果不足，亟需自动化的高效检测方案

### 方法关键点
模拟人类虚假信息标注员的决策行为构建多智能体系统，核心设计包括：引入认知多样性与知识多样性模拟不同标注员的判断差异，加入共识决策机制整合多智能体输出，采用分层结构对齐人类标注流程；全部基于开源LLM（LLaMA、Qwen、Deepseek等）构建，保证系统透明度，支持不同资源量级的多语言任务

### 关键结果
在覆盖高/中/低资源的4种语言、三类虚假信息检测任务（直接检测、待验证文本识别、可验证事实检测）上，效果优于单LLM，包括GPT-3.5和GPT-4
