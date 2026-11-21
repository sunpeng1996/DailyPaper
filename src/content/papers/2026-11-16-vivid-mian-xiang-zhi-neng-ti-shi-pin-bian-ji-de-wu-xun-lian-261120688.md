---
title: 'VIVID: A Visual Harness for Agentic Video Editing'
title_zh: VIVID：面向智能体视频编辑的无训练视觉管控框架
authors:
- Wenhan Yu
- Zhaoxi Zhang
- Zhilong Tan
- Weikang Li
- Lei Sha
affiliations:
- Beihang University
- Peking University
arxiv_id: '2611.20688'
url: https://arxiv.org/abs/2611.20688
pdf_url: https://arxiv.org/pdf/2611.20688
published: '2026-11-16'
collected: '2026-11-21'
category: Agent
direction: Agent 多模态工具增强 视频编辑
tags:
- Agent
- Tool Augmentation
- Multimodal Perception
- Video Editing
- Code Agent
one_liner: 无需额外训练为通用编码Agent提供多模态感知与证据管理能力，大幅提升视频编辑任务表现
practical_value: '- 无需微调大模型、仅通过外挂领域专属工具链+证据记忆机制扩展Agent跨模态能力的思路，可复用在电商短视频生成、商品素材剪辑类业务，大幅降低Agent适配成本

  - 多模态观测结果绑定时空坐标+媒体版本追溯的设计，可迁移到推荐系统多模态内容理解、UGC素材质检类Agent的开发中，提升信息检索准确率

  - 通用Agent+场景专属工具层的轻量化架构，可直接复用在电商内容生成、广告素材自动化加工等场景的Agent落地，无需重新训练领域大模型'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
通用编码Agent具备强理解、推理与代码执行能力，但缺乏适配视频编辑任务的多模态交互、时空信息管理机制，原生能力无法支撑复杂视频编辑需求。
### 方法关键点
VIVID是无训练视觉管控框架，可对接多款原生编码Agent实现视频后期制作，提供按需视频质检、音频分析、转写工具，将观测结果与对应媒体版本、时空坐标绑定存储，支持Agent推理时主动检索，可调用原生编码/Shell工具执行编辑，还能核验渲染输出指导后续迭代。
### 关键结果
在包含组装、修复、排序、二次创作4类共100个任务的AgenticVBench测试集上：
- Codex对接VIVID后平均得分58.6%，较原生版本提升20.2个百分点
- Claude Code、OpenCode对接后得分分别达55.1%、37.1%，均显著优于原生基线
