---
title: 'BLIP-Live: Balancing Timeliness & Firing Precision in Proactive Streaming
  Video Agents'
title_zh: BLIP-Live：平衡主动式流视频Agent响应及时性与触发精度的框架
authors:
- Kanchana Ranasinghe
- Honglu Zhou
- Dominick Reilly
- Le Xue
- Shusheng Yang
- Juan Carlos Niebles
- Silvio Savarese
- Ran Xu
affiliations:
- Salesforce AI Research
arxiv_id: '2611.21553'
url: https://arxiv.org/abs/2611.21553
pdf_url: https://arxiv.org/pdf/2611.21553
published: '2026-11-16'
collected: '2026-11-17'
category: Agent
direction: 主动流视频Agent · 决策平衡优化
tags:
- Proactive Agent
- Streaming Video
- VLM
- Evaluation Metric
- SFT
one_liner: 提出统一数据、度量、推理、训练的主动流视频Agent框架，性能领先基线最高44%
practical_value: '- 直播电商主动导购Agent场景可直接复用PAUC-F度量，同时平衡响应及时性、有效触发精度、重复响应惩罚，避免导购机器人过度打扰用户

  - 离线模型适配流式任务时可复用无训练推理Harness设计：滑动视觉窗口+交互记忆+结构化输出（静默/响应/保持），无需重训即可快速上线流式交互能力

  - 流式决策类Agent的SFT训练可参考样本构造方案：引入Hold状态抑制重复响应、对高占比静默样本做loss masking，避免模型坍缩为全静默同时提升训练效率

  - 时序交互类任务数据集构建可复用「LLM自动生成+人工校验内容+时序区间」 pipeline，大幅降低标注成本同时保证时序决策标注质量'
score: 8
source: arxiv-cs.CV
depth: full_pdf
---

### 动机
主动式流视频Agent需在视频流输入过程中自主判断何时响应、何时静默，现有方案要么只关注响应及时性忽略触发精度，产生大量重复/无效响应，要么度量、数据、优化框架割裂，难以平衡「及时响应」和「不打扰用户」两个核心矛盾目标。

### 方法关键点
- 数据集：BLIP-Live-780K覆盖17.7万条视频共78.5万条主动响应标注，经LLM自动生成+人工校验内容与时序区间，同时标注静默区间，明确监督静默决策
- 度量：PAUC-F指标在传统PAUC的质量加权及时性基础上引入触发精度项，同时惩罚窗口外无效触发和窗口内重复响应，人偏好度达94%以上
- 推理Harness：模型无关的流式适配框架，由滑动视觉窗口、交互记忆（存历史查询与响应）、结构化输出解析三部分组成，无需训练即可将离线VLM适配为流式主动响应模式
- 训练框架：基于SFT的流式训练pipeline，定义静默(S)/响应(R)/保持(H)三类状态，对高占比的静默样本做loss masking，避免模型坍缩为全静默，同时用Hold状态抑制重复响应

### 关键结果
在4个主流主动流视频基准测试中对比20+开源/闭源基线，BLIP-Live-Qwen模型取得SOTA，较最优基线MMDuet2相对提升44%，人偏好度较仅优化PAUC的方案高90%以上。

### 核心结论
流式主动决策类Agent的核心不是尽可能快响应，而是在「及时给出有效响应」和「不发无效/重复信息打扰用户」之间找到最优平衡。
