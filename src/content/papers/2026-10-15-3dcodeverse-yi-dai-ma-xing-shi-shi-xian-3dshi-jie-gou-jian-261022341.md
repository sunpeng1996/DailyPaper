---
title: '3DCodeVerse: Exploring 3D Worlds as Code'
title_zh: 3DCodeVerse：以代码形式实现3D世界构建的研究生态系统
authors:
- Yipeng Gao
- Ziyao Zeng
- Jinfa Huang
- Yijiang Li
- Haolin Xiong
- Wang Qin
- Xinlei Yu
- Youheng Yao
- Jie Zhang
- Kun-Yu Lin
affiliations:
- University of Southern California
- Yale University
- University of Rochester
- University of California, San Diego
- Google DeepMind
arxiv_id: '2610.22341'
url: https://arxiv.org/abs/2610.22341
pdf_url: https://arxiv.org/pdf/2610.22341
published: '2026-10-15'
collected: '2026-10-17'
category: MultiAgent
direction: 多智体协作 · 3D代码自动生成与校验
tags:
- Multi-Agent
- 3D Content Generation
- Code Generation
- Dataset
- Automatic Verification
one_liner: 推出包含2M规模3D代码数据集、多Agent自动校验框架的3D代码化生成全栈生态
practical_value: '- 可复用Multi-Agent DAG编排+自动校验闭环的架构思路，落地到电商3D商品建模、营销素材自动生成业务，大幅降低人工审核与修订成本

  - 垂类代码/内容生成任务的数据集构建可参考「开源数据爬取+异构格式转换+Agent批量生成」的范式，快速扩充高质量垂类训练语料

  - 垂类生成任务效果优化可落地“执行检查+多维度量化反馈+自动迭代”的自监督优化机制，无需人工标注即可持续提升生成准确率'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有3D内容生成方案输出结果可编辑性弱、规模化生产效率低，缺乏标准化可执行3D代码数据集与无人工介入的自动生成校验流程，无法满足批量3D内容生产需求。
### 方法关键点
1. 构建3DCodeVerse-2M数据集：通过开源数据采集、专用表示格式转换、Coding Agent批量生成三种渠道，得到200万条带执行依赖、描述信息、校验记录的独立可执行3D代码样本。
2. 研发3DCodeVerse Harness：基于多Agent DAG框架实现3D内容生成与迭代，通过执行检查、空间测量、视觉反馈三个维度自动校验生成代码，无需人工反馈即可完成自动修订。
3. 完成3D编码任务系统实证：基于数据集微调开源模型搭建基线，通过组件级分析输出3D编码落地实践指导。
### 关键结果
基于Claude Opus 5.5调用时，该框架对比Claude Design (3D Object)的人工 pairwise 评估胜率达90%；基于数据集微调可显著提升开源模型的3D编码能力
