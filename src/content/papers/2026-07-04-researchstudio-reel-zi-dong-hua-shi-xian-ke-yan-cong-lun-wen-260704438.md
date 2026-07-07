---
title: 'ResearchStudio-Reel: Automate the Last Mile of Research from Paper to Poster,
  Video, and Blog'
title_zh: ResearchStudio-Reel：自动化实现科研从论文到海报、视频、博客的最后一公里
authors:
- Lingao Xiao
- Yalun Dai
- Yangyu Huang
- Qihao Zhao
- Wenshan Wu
- Hugo He
- Ruishuo Chen
- Jin Jiang
- Qianli Ma
- Jiahuan Zhang
affiliations:
- Microsoft Research
- National University of Singapore
- Nanyang Technological University
- Tsinghua University
- Peking University
arxiv_id: '2607.04438'
url: https://arxiv.org/abs/2607.04438
pdf_url: https://arxiv.org/pdf/2607.04438
published: '2026-07-04'
collected: '2026-07-07'
category: Agent
direction: Agent 多技能组合自动化工作流
tags:
- Agentic Workflow
- Skill Composition
- Document Automation
- Multi-Artifact Generation
- LLM Agent
one_liner: 提出5个模块组成的Agent流水线，一次性将论文转为可编辑海报、视频、双语博客及统一交互viewer
practical_value: '- 多输出Agent流水线可复用共享抽取层设计，在商品详情页转短视频、海报、推广文案的生成场景中，避免重复抽取信息导致的事实不一致，降低计算成本

  - 可借鉴硬过检门替代软打分的质量控制方案，生成广告文案、商品素材时，用可量化硬规则（如文案长度、图片占比）替代模糊的VLM偏好打分，减少不符合业务要求的输出

  - 可编辑原生格式输出的思路可迁移到电商素材生成场景，生成的海报、文案直接输出PPT/Word格式，方便运营二次修改，降低落地阻力

  - 统一ID对齐思路可用于多模态内容检索场景，将图文、视频、文案通过统一ID绑定，实现点击任意模态内容跳转关联内容的交互体验'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有科研成果传播的最后一公里（论文转海报、宣讲视频、科普博客）完全依赖人工，现有自动化方案均为单场景孤立实现，存在重复抽取信息导致事实不一致、输出为不可编辑的单向渲染文件、用软VLM偏好打分做质量控制容易出现核心内容缺失三类问题，同时缺乏统一的交互载体打通三类产出物。

### 方法关键点
- 采用5个模块化Agent技能的流水线架构：上游共享抽取层Paper2Assets仅做一次信息提取，输出包含文本、图表、元数据、结构化摘要的统一资产包，供下游三个生成器复用，保证多输出事实一致
- 三个生成器分别输出可原生编辑的文件：Paper2Poster输出可编辑PPT格式海报、Paper2Video输出带时间轴的PPT+双版本视频、Paper2Blog输出中英双语可编辑Word格式博客，所有生成环节采用硬过检门替代软打分，仅当布局填充率、图表占比、时长符合预设阈值才输出
- 新增Paper2Reel交互收敛层，通过统一ID绑定海报区块、视频片段、博客段落，实现交互式浏览，点击任意区块自动跳转其余模态对应内容

### 关键实验
在Paper2Poster基准的100篇论文集上对比单shot大模型、现有自动化海报系统、作者自制海报，生成海报在VLM打分的美观度上超出作者自制0.58/5分，在84%~93%的论文上整体得分优于所有对比方案，是唯一同时支持三类可编辑产出物的流水线。

### 最值得记住的一句话
复杂多输出Agent工作流的核心优化点不在于单个环节的生成效果，而在于共享上游资产降低重复劳动、硬规则过检门提升输出确定性、原生格式输出降低用户使用门槛的组合设计。
