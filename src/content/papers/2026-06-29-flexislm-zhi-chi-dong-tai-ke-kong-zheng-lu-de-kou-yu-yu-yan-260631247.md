---
title: 'FlexiSLM: A Dynamic and Controllable Frame Rate Spoken Language Model'
title_zh: FlexiSLM：支持动态可控帧率的口语语言模型
authors:
- Jiaqi Li
- Chaoren Wang
- Xiaohai Tian
- Mingjie Chen
- Xinyu Liang
- Xu Li
- Yufan Lin
- Junwen Qiu
- Jun Zhang
- Lu Lu
affiliations:
- The Chinese University of Hong Kong, Shenzhen
- ByteDance
arxiv_id: '2606.31247'
url: https://arxiv.org/abs/2606.31247
pdf_url: https://arxiv.org/pdf/2606.31247
published: '2026-06-29'
collected: '2026-07-02'
category: LLM
direction: 口语大模型 · 动态帧率优化
tags:
- SLM
- Dynamic Frame Rate
- Inference Optimization
- Speech Understanding
- Controllable Generation
one_liner: 首次实现输入输出均支持动态可控帧率的口语大模型，同参数量下效果优于主流固定帧率SLM且可灵活权衡推理速度与质量
practical_value: '- 可复用动态帧率思路优化多模态Agent的语音交互推理速度，在电商语音客服、语音导购场景下根据算力资源动态调整帧率，平衡交互效果与响应延迟

  - 语音类推荐场景（如有声内容推荐、语音push）可借鉴该方法降低ASR/TTS链路推理成本，高并发时段降帧率保服务可用性

  - 多模态LLM接入推荐系统时，可参考动态token压缩思路，对非核心语音信息降采样减少上下文占用，提升大模型推理效率'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有SLM采用固定帧率编码语音，忽略语音信息密度的时变特性，推理阶段无法灵活在质量与速度间做权衡，动态帧率语音编码技术此前未落地到SLM场景。
### 方法关键点
提出FlexiSLM，是首个在语音输入、输出双端均支持动态可控帧率的SLM，适配动态帧率语音编码技术与LLM backbone，实现帧率的精准可控调节。
### 关键结果
高质量档位下效果优于同7B参数级的Qwen2.5-Omni、Kimi-Audio等固定帧率SLM；帧率最低可稳定调控至4.0Hz，6.25Hz档位下相对12.5Hz帧率推理时间减半，同时保持优秀的语音交互质量。
