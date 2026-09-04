---
title: 'Beyond Retrieval: Progressive Latent Memory Evolution for Streaming Video
  Understanding'
title_zh: 超越检索：面向流媒体视频理解的渐进式隐空间记忆演化框架
authors:
- Hongyu Qu
- Guangming Yao
- Ling Xing
- Xiaobin Hu
- Rongxing Ding
- Guibin Zhang
- Fan Zhang
- Yi Yuan
- Xiangbo Shu
- Shuicheng Yan
affiliations:
- Nanjing University of Science and Technology
- Ant Group
- National University of Singapore
- The Chinese University of Hong Kong
arxiv_id: '2609.04131'
url: https://arxiv.org/abs/2609.04131
pdf_url: https://arxiv.org/pdf/2609.04131
published: '2026-09-02'
collected: '2026-09-04'
category: Multimodal
direction: 多模态大模型 · 流式记忆优化
tags:
- Streaming-Video-Understanding
- MLLM
- Latent-Memory
- Test-Time-Optimization
- Memory-Management
one_liner: 提出无需微调MLLM的retrieve-and-internalize隐记忆框架LatentStream，刷新流媒体视频理解SOTA
practical_value: '- 电商直播实时理解、短视频流审核场景可复用三级分层流存储架构，通过Jenks自适应压缩历史视觉特征，在固定内存预算下保留高价值信息，降低长时流推理成本

  - 电商导购Agent、多轮交互推荐系统可借鉴retrieve-and-internalize范式，将检索到的用户历史行为、对话上下文内化到固定长度的隐空间记忆token中，避免context窗口无限膨胀

  - 可复用基于预测熵的置信度奖励做测试时优化，无需微调基座大模型即可快速适配特定业务任务，适配业务快速迭代需求'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有流媒体视频理解方案均采用store-and-retrieve范式，仅将检索到的历史视觉信息作为外部上下文注入MLLM，无法内化到紧凑的隐空间状态中持续指导后续推理，导致长序列下内存与计算开销随时间线性增长，且历史记忆与查询推理的耦合度极低，效果天花板明显。
### 方法关键点
- 构建Query无关的三级分层流存储（HSM）：将视觉历史分为短/中/长期三级，通过Jenks自然断点法自适应做时序修剪和空间特征合并，在固定token预算下保留多粒度高价值历史信息
- 分层隐记忆演化（HME）：设计三组对应不同感受野的Latent Memory Tokens（LMTs），迭代检索对应存储域的历史证据，将信息逐步内化为固定长度的隐状态
- 渐进式置信度引导优化（PMO）：基于分组预测熵构建分层奖励，在测试时联合优化LMTs与检索到的特征，全程无需微调基座MLLM参数
### 关键结果
基于Qwen2.5-VL-7B基座测试，在OVO-Bench流式基准上整体得分**64.2%**（较基线提升10.2个百分点），StreamingBench得分**76.9%**（较基线提升3个百分点）；同时峰值内存降低28.7%，单token解码延迟降低51%，在离线长视频基准上也取得一致增益。
### 核心结论
流式记忆的优化方向可从传统store-and-retrieve转向retrieve-and-internalize，将外部检索到的证据内化为固定长度的隐空间状态，可同时兼顾推理效果与资源效率
