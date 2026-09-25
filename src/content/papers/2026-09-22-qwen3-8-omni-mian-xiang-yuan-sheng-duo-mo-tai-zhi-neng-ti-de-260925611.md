---
title: 'Qwen3.8-Omni: Towards Native Omni-Modal Agents'
title_zh: 《Qwen3.8-Omni：面向原生多模态智能体的模型与开源工具链》
authors:
- Qwen Team
affiliations:
- Alibaba Group Qwen Team
arxiv_id: '2609.25611'
url: https://arxiv.org/abs/2609.25611
pdf_url: https://arxiv.org/pdf/2609.25611
published: '2026-09-22'
collected: '2026-09-25'
category: Agent
direction: 原生多模态智能体 · 工具链与长上下文
tags:
- MoE
- Multimodal Agent
- Long Context
- Tool Use
- Open Source
one_liner: 推出原生多模态MoE模型Qwen3.8-Omni-Flash及配套开源工具链，支持百万token长上下文
practical_value: '- 可复用其「粗到细按需检索」的长视频理解方案，用于电商短视频卖点提取、UGC内容结构化、带货内容审核，token消耗降低超45%

  - 开源Qwen-MM-Plugins可直接集成到电商智能客服系统，支持用户发送语音/图片/视频咨询的全模态交互应答

  - 多教师蒸馏跨模态能力整合方法可迁移至多模态推荐模型训练，避免不同模态任务干扰，降低多任务SFT成本

  - 百万token长上下文+MoE架构设计可用于长会话用户行为序列建模，适配直播/长视频内容的个性化推荐场景'
score: 9
source: arxiv-cs.MM
depth: full_pdf
---

### 动机
现有多模态智能体多侧重感知能力，缺乏视频类生产场景所需的全局规划、时序推理、内容质量评估能力，长视听内容全量处理token成本极高，主流Agent框架原生不支持音视频流输入，多模态生产力场景落地困难。

### 方法关键点
- 架构：基于Qwen3.8-Next稀疏MoE主干，搭配视觉、通用音频、空间音频3个独立编码器，显式保留时序信息，原生上下文窗口256K，后扩展至1M token
- 训练：四阶段预训练（编码器对齐→全模态联合训练→QSA稀疏注意力预热→稀疏注意力联合优化），后训练采用多教师蒸馏+跨模态强化学习，整合多领域能力避免跨模态干扰
- 配套工具：开源Qwen-MM-Plugins轻量插件框架（支持音视频摘要、按需懒加载、技能提取等工具）、Qwen-Live-Harness实时多模态智能体框架
- 推理优化：采用粗到细的按需证据检索策略，长视频理解可调度子Agent并行分析，大幅降低token消耗

### 关键结果
- 对比前作Qwen3.5-Omni-Plus，29项音频/视听/Agent任务平均得分提升超25%，每小时音频、视听内容API输入成本分别降低98%、93%
- 多模态Agent任务上，WildClawBench-MM得分从34.5提升至71.0，AgenticVBench从14.5提升至36.8
- 长视频理解Agent模式对比静态模式，OmniVideoBench准确率从63.4提升至67.8，单query token消耗降低45.7%，LVOmniBench准确率反超Gemini 3.8 Flash 2.9个百分点

### 核心结论
多模态大模型的理解能力短板可通过Agentic按需证据检索策略弥补，在降低推理成本的同时实现效果提升
