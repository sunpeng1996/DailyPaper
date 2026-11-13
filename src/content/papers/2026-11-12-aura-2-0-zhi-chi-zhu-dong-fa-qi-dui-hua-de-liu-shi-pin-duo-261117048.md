---
title: 'AURA 2.0: From User-Driven Responses to Model-Initiated Conversations in Streaming
  Video'
title_zh: AURA 2.0：支持主动发起对话的流视频多模态大语言模型
authors:
- Shuhan Li
- Huankang Guan
- Xintong Guo
- Yang Bo
- Yuyang He
- Dunyuan Xu
- Jingyan Chen
- Fang Liu
- Tsz Kin Wan
- Jinpeng Chen
affiliations:
- Huawei Research
- CUHK MMLab
- HKUST
arxiv_id: '2611.17048'
url: https://arxiv.org/abs/2611.17048
pdf_url: https://arxiv.org/pdf/2611.17048
published: '2026-11-12'
collected: '2026-11-13'
category: Multimodal
direction: 多模态流视频交互 · 主动对话
tags:
- Streaming VideoLLM
- Proactive Interaction
- Tool Calling
- Visual Grounding
- Long-Horizon Memory
one_liner: 开源流视频LLM，新增主动对话、流感知工具调用、交互视觉grounding三大能力，性能领先同级别开源模型
practical_value: '- 主动触发策略可直接迁移到直播电商互动Agent：基于实时流（直播画面/评论）识别高价值互动时机，主动给用户发商品提醒、优惠告知，避免无效打扰，提升转化

  - 长时交互记忆（LHIM）的分层压缩方案可复用在长会话推荐场景：将超出滑动窗口的历史行为/交互内容转成结构化QA对存储，既降低上下文长度压力，又保留关键历史信息

  - 类别不平衡的响应控制损失设计可借鉴到静默/响应二分类场景：用focal loss+类别均衡归一化处理沉默样本远多于响应样本的问题，提升低占比关键决策的准确率

  - 低延迟推理优化技巧可复用在实时交互系统：包括会话级KV缓存复用、静默输出快速截断、句子级TTS并行生成，能显著降低端到端响应延迟'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有流视频LLM完全依赖用户查询触发响应，即便视频流中出现高价值互动机会也保持静默，无法适配直播陪伴、实时助手等需要主动交互的场景，同时缺少流感知工具调用、多轮视觉定位能力，交互效率低。
### 方法关键点
- 三大核心交互能力：MIC自主识别视频流中高价值话题，无用户查询时主动发起对话；SATC结合实时视觉+对话上下文调用外部工具，结果融入交互；IVG支持用户标框提问、模型输出帧对齐bounding box关联回答与具体物体
- 训练方案：构建114亿token、5400小时视频的专属流交互数据集，采用三阶段渐进式SFT，先夯实基础QA+工具调用，再引入主动对话+视觉定位，最后做多能力融合；针对沉默样本占比超94%的不平衡问题，对<|silent|>/<|respond|>控制token用focal loss+类别均衡归一化优化
- 长时记忆与推理优化：新增LHIM，将超出30秒滑动窗口的视频内容转成带时间戳的QA对分层压缩存储，保留长时上下文；推理侧做会话级KV缓存复用、静默输出快速截断、句子级TTS并行，降低延迟
### 关键结果
在4个公开流基准上性能领先所有开源流模型：PhoStream整体得分65.69，超最强专有基线Doubao-Seed-1.8 9.54分；IPIBench主动任务管理平均得分24.99，超次优开源模型13.53分；StreamArena主动交互准确率12.8%，较AURA 1.0提升9.1pct；MIC能力在内部测试集触发率达80%，响应质量得分4.1/5。
### 核心结论
主动交互的核心不是高频触发，而是在正确的时机输出对用户有价值的内容，同时避免无效打扰。
