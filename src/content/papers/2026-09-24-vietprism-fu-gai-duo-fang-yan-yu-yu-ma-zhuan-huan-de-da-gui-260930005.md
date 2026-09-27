---
title: 'VietPrism: A large-scale Vietnamese speech and deepfake corpus with diverse
  dialects and code-switching'
title_zh: VietPrism：覆盖多方言与语码转换的大规模越南语语音及深度伪造语料库
authors:
- Minh Hoang
- Thai Le
affiliations:
- Independent Researcher
- Indiana University, Bloomington, USA
arxiv_id: '2609.30005'
url: https://arxiv.org/abs/2609.30005
pdf_url: https://arxiv.org/pdf/2609.30005
published: '2026-09-24'
collected: '2026-09-27'
category: Other
direction: 多语种语音语料构建 · 音频深度伪造检测
tags:
- SpeechDataset
- DeepfakeDetection
- MultilingualCorpus
- ASR
- AntiSpoofing
one_liner: 发布首个整合转录、说话人、多方言、越英语码转换的大规模越南语开源语音+深度伪造语料库
practical_value: '- 面向越南市场出海的电商/内容平台，可复用该语料优化越南语语音搜索ASR、直播深度伪造音频审核能力

  - 多维度标注语料+配对生成伪造样本的构建范式，可迁移用于小语种语音AI系统的训练/评估数据集建设

  - 跨语种预训练模型在低资源语言、多方言/语码转换场景下的鲁棒性评估方法，可复用在出海业务模型验证流程'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有越南语语音语料多为ASR场景设计，缺少说话人标识、方言、语码转换、深度伪造维度标注，无法支撑多任务语音建模与深度伪造检测研究。
### 方法关键点
1. 采集8388条真实视频中1262名验证说话人的993.4小时、403941条真实语音，覆盖5类方言、近一半时长的自然越-英语码转换，同步提供转录、统一说话人ID标注
2. 基于4款开源/商用语音合成系统生成3100+小时伪造语音，每条伪造样本均匹配对应真实说话人的同转录真实语音，消除词汇、身份混淆变量
### 关键结果
5款零样本多语种深度伪造检测器表现出明显脆性：DFA-1B模型等错误率（EER）随说话人相似度升高从16.3%升至33.6%，不同方言下检测效果差异显著
