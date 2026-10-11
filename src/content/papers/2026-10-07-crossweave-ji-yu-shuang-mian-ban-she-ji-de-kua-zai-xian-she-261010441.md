---
title: 'CrossWeave: Bridging Perspectives Across Online Communities with a Dual-Pane
  Design'
title_zh: CrossWeave：基于双面板设计的跨在线社区观点打通系统
authors:
- Fei Fang
- Reva Hirave
- William Jurayj
- Yuqi Li
- Brian Lu
- Tarik Metin
- Tsugunobu Miyake
- Kateryna Morhun
- Yash Permalla
- Kenan Rustamov
affiliations:
- Johns Hopkins University
- Princeton University
- Georgia Institute of Technology
- Massachusetts Institute of Technology
- Northwestern University
arxiv_id: '2610.10441'
url: https://arxiv.org/abs/2610.10441
pdf_url: https://arxiv.org/pdf/2610.10441
published: '2026-10-07'
collected: '2026-10-11'
category: RecSys
direction: 跨社区内容推荐 · 信息茧房破解
tags:
- Cross-Community Recommendation
- Echo Chamber Mitigation
- LLM Application
- Dual-Pane UI
- Constructive Interaction
one_liner: 推出AI驱动的双面板跨社区内容推荐系统，打破信息茧房促进建设性互动
practical_value: '- 双栏信息流设计可复用在电商种草/内容场景：用户浏览某类商品/内容时，侧边栏推送不同圈层的差异化相关内容，拓展用户视野提升交叉转化

  - 跨池差异化召回逻辑可直接迁移：基于当前浏览内容的语义特征，从多圈层内容/商品池召回高相关且属性/观点差异大的候选，避免推荐同质化

  - 内容发布辅助机制可用于UGC场景：用户撰写评价/晒单/帖子时，预展示潜在受众反馈，引导产出更客观的优质内容，提升社区整体质量'
score: 4
source: arxiv-cs.IR
depth: abstract
---

### 动机
现有社交媒体信息流默认展示同圈层熟人的相关对话，内容同质化严重，长期使用会固化用户认知分歧，扭曲公众舆论感知，在公共议题讨论场景下负面影响尤为突出。
### 方法关键点
1. 创新双面板交互架构：主面板保留原有常规信息流，侧边面板自动从其他社区线程中召回与当前阅读帖语义相关、观点差异化的内容，高亮两者关联点引导用户跨社区探索
2. 内置LLM辅助发帖功能：用户跨社区互动撰写内容时，自动展示相关历史参考内容，模拟发布后的潜在受众反馈，引导用户产出更具建设性的发言
### 关键结果
已完成完整系统实现，可无缝集成到现有社交媒体信息流架构中，核心功能覆盖跨社区内容匹配、关联关系高亮、发帖辅助三大模块
