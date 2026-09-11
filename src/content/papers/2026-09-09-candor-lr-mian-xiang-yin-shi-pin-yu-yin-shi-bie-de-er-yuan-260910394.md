---
title: 'Candor-LR: A Dyadic Conversational Dataset for Audio-Visual Speech Recognition'
title_zh: Candor-LR：面向音视频语音识别的二元对话数据集
authors:
- Rishabh Jain
- Aristeidis Papadopoulos
- Zhaofeng Lin
- Naomi Harte
affiliations:
- Sigmedia Group, School of Engineering, Trinity College Dublin, Ireland
arxiv_id: '2609.10394'
url: https://arxiv.org/abs/2609.10394
pdf_url: https://arxiv.org/pdf/2609.10394
published: '2026-09-09'
collected: '2026-09-11'
category: Multimodal
direction: 多模态音视频识别 · 对话基准数据集
tags:
- Multimodal
- SpeechRecognition
- BenchmarkDataset
- AudioVisual
- Robustness
one_liner: 发布包含783.7小时真实二元对话的音视频语音识别基准数据集，提升模型跨域鲁棒性
practical_value: '- 开发电商语音客服、直播内容理解等对话类Agent时，可引入该数据集微调ASR模块，提升对话重叠、嘈杂环境下的识别准确率

  - 构建业务定制数据集时可参考其处理pipeline，优先覆盖真实场景的噪声、口语化、交互重叠等边缘case，提升模型落地鲁棒性

  - 多模态交互Agent可复用其验证的「视觉特征可有效补偿音频识别降效」结论，叠加唇动等视觉特征优化语音识别性能'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有AVSR基准数据集多为干净脚本化内容，未覆盖真实对话的重叠语音、自发轮次、非脚本词汇、多变声学条件等特性，无法验证模型在现实场景的鲁棒性。
### 方法关键点
基于CANDOR语料库的1656场自然二元视频会议构建Candor-LR基准，自定义数据处理pipeline产出713.5小时训练集、10.1小时验证集、60.1小时测试集，开源全流程保障可复现。
### 关键结果数字
1. 预训练AVSR模型在Candor-LR上的纯音频识别准确率较LRS3大幅下降，但视觉特征带来的性能增益远高于LRS3场景；
2. 基于该数据集训练的模型在干净/噪声场景下的跨域鲁棒性均显著提升。
