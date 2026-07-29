---
title: 'Child-Oriented AIGC Video Risk Reviewing: A Benchmark and Knowledge-Supported
  Iterative Reasoning Framework'
title_zh: 面向儿童的AIGC视频风险审核：基准与知识增强迭代推理框架
authors:
- Lewen Mi
- Manyi Li
- Yuling Sun
- Yufan Zhang
- Yuxin Shi
- Yulong Bian
- Xiangxian Li
- Juan Liu
affiliations:
- Shandong University
- Fudan University
- Beijing Jiaotong University
arxiv_id: '2607.22715'
url: https://arxiv.org/abs/2607.22715
pdf_url: https://arxiv.org/pdf/2607.22715
published: '2026-07-21'
collected: '2026-07-29'
category: MultiAgent
direction: 多Agent 多模态内容风险审核
tags:
- AIGC Moderation
- Multi-Agent
- Benchmark
- Multimodal Reasoning
- Knowledge Augmentation
one_liner: 构建儿童向AIGC视频风险审核基准，提出多Agent知识增强的迭代推理审核框架
practical_value: '- 做UGC/AIGC内容合规审核场景可复用「多Agent+外部专家知识」的迭代推理架构，提升细粒度隐性风险识别准确率

  - 垂直场景风险检测可参考层级化标签体系构建方法，自上而下定义粗-细粒度分类标准适配不同审核粒度需求

  - 多模态内容审核任务可借鉴证据链采集-决策验证的两阶段流程，降低大模型幻觉，提升审核结果可解释性'
score: 7
source: arxiv-cs.MM
depth: abstract
---

### 动机
AIGC视频快速普及，现有通用视频安全检测多从成人视角设计，无法识别儿童观看时面临的细粒度、隐性、场景依赖的发展适配风险，缺乏专项基准与有效审核方案。

### 方法关键点
1. 构建CAVSR基准，包含605条多平台真实儿童向AIGC视频，配套6大类、26个细粒度标签的层级化风险分类体系；
2. 提出QVRS-E知识增强审核框架，融合多Agent协作、专家/经验知识库，实现定向证据采集与基于事实的审核决策。

### 关键结果
结合视觉语言模型的方案相比基线显著提升儿童相关风险审核效果，输出的审核报告鲁棒性更强。
