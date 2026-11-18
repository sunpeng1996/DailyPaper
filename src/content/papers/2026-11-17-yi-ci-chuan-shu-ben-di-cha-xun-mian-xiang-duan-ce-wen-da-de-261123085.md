---
title: 'Transfer Once, Ask Locally: Compact Audio-Visual Memory for On-Device Question
  Answering'
title_zh: 一次传输本地查询：面向端侧问答的紧凑型音视频记忆模块
authors:
- Qitong Wang
- Jihui Jin
- Divya Kothandaraman
- Vishnu Raj
- Christopher Rasmussen
affiliations:
- Dolby Laboratories, Inc.
- University of Delaware
arxiv_id: '2611.23085'
url: https://arxiv.org/abs/2611.23085
pdf_url: https://arxiv.org/pdf/2611.23085
published: '2026-11-17'
collected: '2026-11-18'
category: Multimodal
direction: 多模态大模型 · 端侧推理token剪枝
tags:
- Multimodal-LLM
- Token-Pruning
- On-Device-Inference
- Shapley-Value
- Audio-Visual-QA
one_liner: 训练无关无查询感知的音视频token剪枝框架，构建可复用记忆实现端侧QA精度效率双升
practical_value: '- 可复用跨模态记忆构建思路可迁移到电商短视频/直播场景的端侧智能导购：服务端预剪枝多模态特征后一次下发，端侧无需回传用户查询即可完成多轮问答，既保护隐私又降低传输和推理开销

  - 基于蒙特卡洛Shapley值的无查询感知token选择方法可复用在生成式推荐的特征压缩场景：无需用户query即可预筛选高价值的物品/内容特征，降低RAG召回和LLM推理成本

  - 跨模态冗余校准机制可直接用于电商多模态内容理解：对图文、音视频等多模态输入的重复信息降权，在特征压缩时优先保留互补信息，提升下游召回/排序精度'
score: 8
source: arxiv-cs.CV
depth: full_pdf
---

### 动机
端侧音视频问答面临隐私、传输成本、端侧算力的三重约束：全链路服务端部署需要回传用户查询存在隐私风险，全端侧部署算力无法支撑大模型推理，现有模型拆分方案下全量多模态特征传输和推理开销依然过高，且无法在无用户查询的情况下预构建可复用的特征内存。

### 方法关键点
- 训练无关、无查询感知的剪枝框架：将视频时空块、对齐的音频时间窗作为独立player，筛选后保留原始token embedding而非压缩特征，可支撑多轮本地QA复用
- 蒙特卡洛Shapley值评估player重要性：基于embedding覆盖度目标函数，兼顾单模态效用（token embedding L2 norm均值作为语义信息量代理）和跨模态冗余校准（对齐跨模态player的余弦相似度越高权重越低）
- 动态模态预算分配：根据音视频各自的聚合效用值分配剪枝预算，适配不同内容的模态重要性差异

### 关键结果
在Video-MME、Daily-Omni、Video-Holmes三个基准数据集上，对比DivPrune、VisionZip、OmniZip三个SOTA剪枝方案，基于video-SALMONN 2+（3B）和2 Pro（4B）backbone测试：80%剪枝率下，Daily-Omni数据集上精度比基线高12.86-14.62个百分点，端侧LLM解码速度最高提升1.92倍，embedding内存占用降低79.8%；90%剪枝率下依然保持SOTA精度。

**最值得记住的一句话**：无查询感知的跨模态特征预剪枝可以在几乎不损失下游任务精度的前提下，大幅降低端侧多模态交互的传输、内存和计算开销，是端侧多模态智能交互的可行落地方向。
