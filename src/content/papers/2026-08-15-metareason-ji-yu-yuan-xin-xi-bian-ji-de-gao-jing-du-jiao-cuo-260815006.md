---
title: 'MetaReason: Precise Interleaved Multimodal Reasoning via Editing Meta Information
  for Solving Geometry Problems'
title_zh: MetaReason：基于元信息编辑的高精度交错多模态几何推理框架
authors:
- Penghao Yin
- Haomin Wang
- Qihong Tang
- Xiaoye Qu
- Hongjie Zhang
- Xiao-Ping Zhang
affiliations:
- Tsinghua University
- Shanghai AI Laboratory
- Shanghai Jiao Tong University
- Nanjing University
arxiv_id: '2608.15006'
url: https://arxiv.org/abs/2608.15006
pdf_url: https://arxiv.org/pdf/2608.15006
published: '2026-08-15'
collected: '2026-08-21'
category: Reasoning
direction: 多模态推理 · 结构化视觉解析
tags:
- Multimodal Reasoning
- Structured Information Parsing
- Controllable Generation
- Benchmark Dataset
- Visual Reasoning
one_liner: 提出基于元信息编辑的多模态几何推理框架，配套大规模训练数据集与真实考试难度评测基准
practical_value: '- 电商多模态内容理解/审核场景可复用「图像解析为结构化元信息→可控编辑生成高保真增强视图→基于增强特征推理」的链路，降低细粒度视觉识别误差

  - 复杂多步推理Agent可参考SFT+RL结合结构化推理轨迹数据集训练的范式，提升推理链的稳定性与准确率

  - 业务评测体系搭建可借鉴ExamGeo的分层难度设计思路，覆盖不同复杂度的真实业务场景，评测结果更贴合线上表现'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有视觉语言模型在平面几何推理等需细粒度空间感知的场景下，多依赖纯文本推理，或引入的中间视觉状态存在几何表示不准确、渲染保真度低的问题，最终输出可靠性不足。
### 方法关键点
1. 提出MetaReason框架：先将几何图像解析为结构化元信息，通过预定义工具可控编辑合成高保真视觉状态，再基于增强视图完成推理，支持高精度辅助线构造；
2. 构建TutorGeo训练数据集：包含17k图像转元信息样本、60k纯文本推理轨迹、60k交错多模态推理轨迹，采用SFT+RL组合方式训练模型的多模态推理能力；
3. 推出ExamGeo评测基准：基于真实考试题目构建，支持不同难度级别的系统性评测。
### 关键结果
效果显著超越所有现有开源模型，性能与闭源专有模型达到可比水平。
