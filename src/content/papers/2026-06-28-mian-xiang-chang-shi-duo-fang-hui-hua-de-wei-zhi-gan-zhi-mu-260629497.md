---
title: 'Position-Aware Target Speaker Extraction for Long-Form Multi-Party Conversations:
  A Diarization-Free Framework for ASR'
title_zh: 面向长时多方会话的位置感知目标说话人提取：无需分割的ASR框架
authors:
- Yichi Wang
- Junzhe Chen
- Wangjin Zhou
- Tatsuya Kawahara
affiliations:
- Graduate School of Informatics, Kyoto University
arxiv_id: '2606.29497'
url: https://arxiv.org/abs/2606.29497
pdf_url: https://arxiv.org/pdf/2606.29497
published: '2026-06-28'
collected: '2026-07-04'
category: Other
direction: 多方会话语音识别 · 无分割ASR框架
tags:
- ASR
- Target Speaker Extraction
- DOA
- Multi-Party Conversation
- Diarization-Free
one_liner: 基于DOA空间先验实现无需说话人分割的目标说话人提取，提升长时多方会话ASR效果
practical_value: '- 电商智能客服、直播多人连麦场景的ASR转写链路，可借鉴DOA空间先验思路，省略显式说话人分割步骤，降低链路复杂度与延迟

  - 多人会议式带货、主播连麦互动的用户语义/意图识别任务，可复用该前端输出的分说话人流，减少说话人对齐误差，提升转写准确率

  - 面向会话式Agent的多用户语音交互场景，可直接对接该框架输出，快速实现多说话人语音的分离与归因，降低业务开发成本'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
长时多方会话存在说话人活动不均衡、语音频繁重叠问题，传统滑动窗口连续语音分离（CSS）方案存在跨窗口说话人身份不一致、残留串扰缺陷，需额外依赖说话人分割才能完成说话人归因，链路复杂且效果受限。
### 方法关键点
基于会议/线下会话场景说话人到达角（DOA）稳定的特性，提出PATSE多通道位置感知目标说话人提取前端，融合DOA引导的空间编码器与条件生成器，直接输出各目标说话人对应的独立语音流，仅需VAD等简单后处理即可推断说话人活动，完全无需显式说话人分割模块。
### 关键结果
在回放、真实两类多方会话数据集上，ASR效果均稳定优于CSS基线、以及基于说话人分割的传统pipeline。
