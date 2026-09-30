---
title: LLMs are General Asynchronous Agents
title_zh: 通用异步LLM Agent框架AsyncLLM：无需任务微调适配多实时场景
authors:
- George Yakushev
- Denis Mazur
- Vladimir Bartenev
- Vyacheslav Zhdanovskiy
- Timofey Byzov
- Vladimir Kaurkin
- Vadim Pastushenko
affiliations:
- Yandex
- Together AI
- HSE University
- Yandex School of Data Analysis
arxiv_id: '2609.35427'
url: https://arxiv.org/abs/2609.35427
pdf_url: https://arxiv.org/pdf/2609.35427
published: '2026-09-27'
collected: '2026-09-30'
category: Agent
direction: Agent架构 · 异步LLM推理
tags:
- AsyncLLM
- LLM Agent
- KV Cache
- Asynchronous Inference
- Multimodal Agent
one_liner: 提出支持共享KV cache的异步LLM框架，无需微调适配视频、游戏、监控等多异步场景
practical_value: '- 电商实时智能客服可复用async/await架构，将用户输入监听、语义理解、回复生成分拆为并行协程，原生支持用户中途打断、多并发会话交互，无需额外微调模型

  - 直播/短视频实时内容推荐场景可复用共享KV cache的多协程设计，将帧采样、事件识别、推荐策略触发拆为并行流程，实测吞吐量最高可提升4倍以上

  - 大促/系统实时监控Agent可直接复用日志流处理架构，用多协程并行处理日志流、异常识别、告警触发，比串行方案推理步数减少50%以上，响应速度翻倍'
score: 9
source: huggingface-daily
depth: full_pdf
---

### 动机
现有LLM Agent普遍采用串行Thought-Action-Observation交互循环，无法适配语音助手、实时监控、具身智能等需要边接收输入边思考响应的异步场景；现有异步方案均为单任务定制微调，通用性差、落地成本高，无法快速迁移到新场景。
### 方法关键点
- 基于Python asyncio实现async/await编程模型，支持定义多个并行推理协程，通过CacheBlock存储KV cache、GDN状态等共享内存，协程可通过cache_view访问其他协程的内存状态，无额外通信开销
- 适配混合/多模态LLM：对全注意力层用查询旋转替代KV块旋转降低计算开销，对线性注意力/GDN层设计块级仿射变换组合机制，原生支持MRoPE多模态位置编码
- 推理引擎基于SGLang改造，自动合并协程请求做批量GPU推理，采用分块prefill、优先级调度避免实时请求被长推理任务阻塞
### 关键实验
基于Qwen3.x系列模型，无任何任务特定微调：
1. 流视频理解任务：SoccerNet数据集Trigger Acc达62.82%，比专属训练的Mage-VL高10个百分点；ProactiveVideoQA整体PAUC达0.541，超基线26%
2. ViZDoom游戏任务：响应延迟比同模型串行Agent低60%，同时保留推理带来的收益
3. 系统监控任务：准确率与串行方案相当，推理步数减少54%，响应速度提升100%
### 核心结论
现代LLM本身已具备异步处理能力，无需任务特定微调，仅通过内存共享的异步推理框架即可适配各类实时场景
