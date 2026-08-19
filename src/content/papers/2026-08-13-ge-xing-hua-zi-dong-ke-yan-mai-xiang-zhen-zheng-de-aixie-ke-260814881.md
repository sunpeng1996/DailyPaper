---
title: 'Personalized Auto-Research: Towards a True AI Co-Scientist'
title_zh: 个性化自动科研：迈向真正的AI协同科学家
authors:
- Bo Ni
- Franck Dernoncourt
- Hongjie Chen
- Yu Wang
- Nesreen K. Ahmed
- Zhengzhong Tu
- Tyler Derr
- Ryan A. Rossi
affiliations:
- Vanderbilt University
- Adobe Research
- Dolby Laboratories
- University of Georgia
- Cisco AI Research
arxiv_id: '2608.14881'
url: https://arxiv.org/abs/2608.14881
pdf_url: https://arxiv.org/pdf/2608.14881
published: '2026-08-13'
collected: '2026-08-19'
category: Agent
direction: Agent 科研协同系统个性化优化
tags:
- LLM Agent
- Personalization
- Auto-Research
- Graph Representation
- Human-AI Collaboration
one_liner: 提出基于研究者异质图画像的全流程个性化自动科研通用框架
practical_value: '- 做个性化Agent时可借鉴「异质图+用户多维度信号」的用户画像构建思路，而非仅依赖历史行为，比如电商中把用户的社交关系、浏览内容、消费能力、所处圈层等建模为异质图生成用户表征，提升个性化匹配准确度

  - Agent多步骤决策场景下可借鉴「全链路个性化注入」的设计，把用户上下文注入检索、候选生成、排序、输出全环节，而非仅在最后做重排，比如电商导购Agent在召回商品、生成话术、推荐搭配每一步都带入用户画像

  - 个性化场景的目标函数设计可参考其三维度加权思路：兼顾匹配度、新颖性、可行性，避免过度拟合用户历史导致推荐同质化，比如电商推荐中平衡用户偏好匹配、跨品类新颖性、价格/地域可行性'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有AI自动科研系统均为研究者无感知设计，相同目标给不同研究者输出完全一致的结果，忽略了研究者的过往工作、方法储备、所处学术圈、可支配资源等异质性，既无法匹配不同研究者的落地可行性需求，也容易导致科研方向趋同的 monoculture 问题，不符合科研创新高度依赖研究者隐性知识的本质，个性化绝非附加功能，而是AI协同科学家的核心属性。

### 方法关键点
- 用包含研究者、论文、机构、方法、话题等节点的异质科研图对研究者建模，通过图编码器生成研究者表征，结合其论文、代码、评审历史、偏好等信号生成个性化上下文
- 全链路注入个性化：将用户上下文融入文献检索、假设生成、实验设计、代码执行、论文撰写、引用优化、自动评审全流程的每一步决策，相同目标给不同研究者生成完全不同的搜索路径和输出
- 假设排序目标函数同时加权三个维度：面向领域和研究者的新颖性、和目标的相关性、匹配研究者资源的可行性，避免生成无法落地的方案
- 支持团队个性化扩展：通过聚合团队所有成员的表征生成团队上下文，适配多人协作场景

### 关键结果
为框架性研究，无具体对照实验数据，提出了可自动化的个性化信号验证协议：用t时间前的用户数据生成上下文，验证系统是否能复现用户t时间发表论文的研究路径，且和无个性化基线输出有显著差异。

**最值得记住的一句话**：个性化不是AI协同科学家的便利附加层，而是使其从通用工具成为真正合作者的核心属性
