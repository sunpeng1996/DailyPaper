---
title: 'StreamArena: Toward Continuous, Interactive, and Long-Horizon Agentic Streaming
  Video Understanding'
title_zh: StreamArena：小时级流式视频Agent理解基准与StreamMind双层架构
authors:
- Xichen Zhang
- Guankai Li
- Yinghao Zhu
- Shijian Wang
- Sitong Wu
- Shaozuo Yu
- Meng Chu
- Yuan Lu
- Jiaya Jia
affiliations:
- The Hong Kong University of Science and Technology
- Xiaohongshu Inc.
- The University of Hong Kong
- The Chinese University of Hong Kong
arxiv_id: '2608.05703'
url: https://arxiv.org/abs/2608.05703
pdf_url: https://arxiv.org/pdf/2608.05703
published: '2026-08-05'
collected: '2026-08-10'
category: Agent
direction: 多模态Agent · 长时序流式视频理解
tags:
- Multimodal Agent
- Streaming Video Understanding
- Long-Horizon Memory
- Benchmark
- Two-tier Architecture
one_liner: 首个小时级交互流式视频多模态Agent评测基准，配套双层架构相对基线最高提升228%
practical_value: '- 电商直播场景长时序Agent可直接复用双层架构：前端做实时交互/关键词监控，后端异步构建直播内容记忆库，召回历史商品讲解、用户提问上下文，大幅降低实时响应延迟

  - 长时序多模态系统评测可借鉴StreamArena设计，覆盖实时感知、历史召回、主动触发、工具调用四类核心能力，规避短片段/选择题的评估捷径，更贴近真实业务

  - 长视频/直播内容打标、智能剪辑场景可参考分层记忆设计，存储实体关系、分层事件、关键帧，平衡记忆容量和细粒度信息保留，提升长时序内容召回准确率'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有流式视频理解评测多依赖短片段、选择题形式，存在明显的近帧捷径、语言偏置问题，仅保留最后4帧的简单基线就能超过复杂流式模型；同时现有架构无法同时满足低延迟交互、长时序记忆、主动触发、工具调用四类真实部署需求，无法支撑小时级连续运行的多模态Agent落地。
### 方法关键点
- 构建StreamArena评测基准：包含243条平均88.8分钟的长视频，3646条人工标注的开放式问答对，覆盖实时感知、历史回溯、主动交互、多模态工具调用4类核心能力，所有问答绑定查询、证据双时间戳，严格遵循因果访问规则。
- 提出StreamMind双层架构：前端由独立调度的Front Worker负责实时交互、Monitor Worker做主动事件监控，不阻塞核心响应路径；后端异步构建包含分层事件、实体关系图、关键帧的持久化多模态记忆库，由Router Worker协调Recall、Search Worker完成历史召回、外部工具调用。
### 关键结果
对比5类现有系统，StreamMind在4类能力上均为流式系统最优：相对最强基线，实时感知提升58.4%、历史回溯提升53.7%、工具调用提升228.1%、主动交互提升54.7%；同骨干下整体查询响应延迟降低66.2%，仅损失10.3%的准确率。
### 核心结论
长时序流式多模态系统需要将低延迟交互路径和长时序记忆构建、检索路径解耦，提前预构建持久化多模态记忆比查询时再采样编码的效率高一个量级。
