---
title: 'Error Rate is Not Enough: Costs of Augmentation in Low-Resource ASR'
title_zh: 低资源语音识别数据增强的代价：仅靠错误率评估不足
authors:
- Katsumi Ibaraki
- David Chiang
affiliations:
- University of Notre Dame
arxiv_id: '2610.13807'
url: https://arxiv.org/abs/2610.13807
pdf_url: https://arxiv.org/pdf/2610.13807
published: '2026-10-09'
collected: '2026-10-13'
category: Other
direction: 低资源ASR 数据增强策略优化
tags:
- Data Augmentation
- Low-Resource ASR
- Error Analysis
- Training Strategy
one_liner: 揭示低资源ASR不同数据增强方法的误差互补性，给出训练前可选的增强筛选方案
practical_value: '- 低资源冷启动场景（如新品推荐、小语种语音交互）评估策略不要只看整体指标，必须拆分细分错误/bias类型，避免总指标上涨但核心体验下降的问题

  - 不同数据增强/样本构造策略可通过误差互补性搭配，比如召回侧不同召回通路的bias互补，抵消单通路引入的badcase

  - 低资源场景下可提前计算训练样本的特征曝光度、属性分布，无需全量训练就能预筛选最优策略，降低实验成本'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
低资源ASR场景数据增强是标准操作，但业界普遍仅用总错误率评估收益，无法明确策略生效的原因与适用边界，且特定场景下细分错误类型的影响远大于总错误率。
### 方法关键点
在4种低资源语言、5种不同数据量的英语ASR任务上，交叉验证2种原生音频修改增强（速度扰动、SpecAugment）与2种文本转录合成音频增强的效果，做音素级的错误拆解分析。
### 关键结果
- SpecAugment的总错误率提升最稳定，但会升高声调、腭化音错误；文本类增强会引入辅音插入错误，二者组合可互相抵消对方引入的错误
- 文本类增强可将低频音素的出现频率提升37~38%，逆转对应类型的识别错误
- 组合增强的收益超过单个策略收益之和，该超加性在训练数据量达到100小时后消失，仅在低资源场景生效
