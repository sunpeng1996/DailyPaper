---
title: 'AskStream: When and What to Ask Proactively under Uncertainty in Streaming
  Video Understanding'
title_zh: AskStream：流式视频理解不确定场景下的主动提问时机与内容决策基准
authors:
- Lu Wang
- Zhuoran Jin
- Longxiang Wang
- Junhong Chen
- Yupu Hao
- Yao Xu
- Daojian Zeng
- Yubo Chen
- Kang Liu
- Guang Liu
affiliations:
- 中国科学院自动化研究所
- 北京人工智能研究院(BAAI)
- 湖南师范大学
- 中央民族大学
arxiv_id: '2610.38678'
url: https://arxiv.org/abs/2610.38678
pdf_url: https://arxiv.org/pdf/2610.38678
published: '2026-10-28'
collected: '2026-10-30'
category: Agent
direction: Agent 流式视频主动交互能力评测
tags:
- Proactive Agent
- Multimodal LLM
- Streaming Video
- Benchmark
- Uncertainty Handling
one_liner: 首个支持三元主动动作的流式视频理解基准，覆盖视频与用户两类不确定性
practical_value: '- 主动交互决策框架可迁移到直播导购Agent：将wait/ask/answer三元决策逻辑适配到直播场景，识别商品信息缺失、用户意图模糊时主动提问（比如用户说“给我看看那个包”时主动确认款式），避免无效等待或错误应答

  - Ask-F1时序感知评价指标可复用：针对主动交互类系统（比如智能客服、直播助手）的时序决策效果评估，同时覆盖动作内容正确性与触发时机合理性

  - StreamHarness分层内存架构可直接用于长流式场景：比如直播/长视频内容理解场景，分层存储近期帧、中期摘要、长期压缩记忆，平衡内存占用与上下文保留率

  - 不确定性分类框架可复用：将业务场景的不确定性划分为内容侧（商品/素材）与用户侧（意图/偏好）两类，针对性设计主动提问触发策略'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有流式视频主动交互范式仅支持wait/answer二元动作，默认回答所需信息必然会在流中出现，忽略真实场景普遍存在的信息不完备问题：要么来自视频侧的证据缺失、个性化概念缺失，要么来自用户侧的意图模糊、偏好缺失，会导致模型无限等待或生成幻觉，缺乏主动索要缺失信息的能力，且无对应评测基准。

### 方法关键点
- 提出三元主动交互范式，新增ask动作，允许模型主动向用户/系统索要缺失信息
- 构建AskStream多轮基准，覆盖视频、用户两类不确定性下的4大类任务8个子任务，包含438条视频、2714个帧级标注的wait/ask/answer时间窗口
- 设计Ask-F1指标，联合评估提问/回答的内容正确性与触发时机合理性
- 提出StreamHarness分层内存框架，分层存储近期帧、中期摘要、长期压缩记忆，适配流式视频长上下文理解需求

### 关键实验
对比三类模型：1）闭源离线MLLM（GPT-5.6-Sol、Gemini-3.8 Flash等），最优Gemini-3.8 Flash Ask-F1仅52.18%；2）开源离线MLLM，最优DeepSeek-V4.1-Flash Ask-F1仅19.69%；3）流式主动模型，最优AURA Ask-F1仅7.22%；消融实验显示提供提问时机的先验信息可提升Ask-F1 21.13个百分点，提问时机决策是当前最大瓶颈。

### 核心结论
当前多模态大模型的主动信息获取能力远未达标，何时提问比问什么、何时回答的瓶颈更突出。
