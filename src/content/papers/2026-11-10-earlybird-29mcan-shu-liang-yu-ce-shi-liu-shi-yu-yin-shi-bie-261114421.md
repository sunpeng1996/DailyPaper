---
title: 'Earlybird: Predictive Streaming Speech Recognition in 29M Parameters'
title_zh: Earlybird：29M参数量预测式流式语音识别模型
authors:
- Sahil Mahendrakar
arxiv_id: '2611.14421'
url: https://arxiv.org/abs/2611.14421
pdf_url: https://arxiv.org/pdf/2611.14421
published: '2026-11-10'
collected: '2026-11-12'
category: Agent
direction: 语音Agent低延迟流式ASR优化
tags:
- Streaming ASR
- Voice Agent
- Low Latency
- Small Model
- Confidence Calibration
one_liner: 29M参数量流式ASR可在用户说完单词前中位90ms正确预测，大幅降低语音Agent响应延迟
practical_value: '- 语音购物/语音搜索场景可复用随机截断音频训练范式，降低ASR延迟，让搜索召回提前启动，缩短端到端响应时长

  - 小参数ASR的置信度校准方案可直接复用，用于判断提前预测的query是否可靠，避免错误触发召回浪费资源

  - 29M参数4bit量化后仅16.8MB，可直接部署在端侧设备，适合IoT/APP端语音交互场景，降低云端算力成本'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有流式ASR需等用户说完单词才输出，延迟90-400ms，拖慢语音Agent的搜索/回复规划速度，端侧部署也需要超小参数轻量化方案。

### 方法关键点
1. 训练时将音频按80ms步长随机截断，即使单词仅播放部分也要求输出完整已出现单词，同时预测后续2个单词
2. 输出原始token概率作为单词置信度，对仍在播报的单词置信度做校准
3. 参数量仅29M，4bit量化后体积16.8MB，适配端侧部署要求

### 关键结果
- LibriSpeech测试集上中位单词预测比用户说完早90ms，现有方案晚90-400ms；69%单词在说完前正确预测，竞品仅3-25%
- 6个不同场景测试集延迟均为最低，8个英文公开ASR榜单上精度优于Moonshine Tiny，和同规模Whistle精度相当
- 正在播报单词的预期校准误差（ECE）仅3.7-5.5
