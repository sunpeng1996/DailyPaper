---
title: Utilizing Cognitive Signals Generated during Human Reading to Enhance Keyphrase
  Extraction from Microblogs
title_zh: Utilizing Cognitive Signals Generated during Human
authors:
- Xinyi Yan
- Yingyi Zhang
- Chengzhi Zhang
arxiv_id: '2606.26485'
url: https://arxiv.org/abs/2606.26485
pdf_url: https://arxiv.org/pdf/2606.26485
published: '2026-06-25'
collected: '2026-06-26'
category: RecSys
direction: RecSys
tags:
- RecSys
- LLM
one_liner: Microblogging platforms generate massive amounts of short, noisy, and dispersed
  user content, m...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 DeepSeek API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 8
source: arxiv-cs.IR
depth: abstract
---

### 摘要

Microblogging platforms generate massive amounts of short, noisy, and dispersed user content, making automatic keyphrase extraction (AKE) an important but challenging task. Prior studies have used eye-tracking signals to improve microblog-based AKE because such signals reflect readers' attention to salient words. However, eye tracking alone is limited by physiological, acquisition, and feature-decoding constraints. To address this issue, we investigate whether electroencephalogram (EEG) signals can complement eye-tracking signals for AKE. Using the ZuCo cognitive language processing corpus, we select 8 EEG features and 17 eye-tracking features and incorporate them into microblog-based AKE models. To reduce possible distortion of cognitive signals by model structures, we inject these features into the input of the soft-attention layer and the query vectors of the self-attention layer. We then evaluate different combinations of cognitive signals across AKE models. The results show that cognitive signals produced during reading consistently improve AKE performance, regardless of feature combinations and model architectures. EEG features bring the largest gains, while combining EEG and eye-tracking features yields performance between the two individual signal types, suggesting partial complementarity but also possible redundancy or noise. These findings indicate that EEG signals provide useful cognitive evidence for microblog-based AKE and that multimodal cognitive signals deserve further investigation.

> 当前运行未检测到 DeepSeek API Key，本卡片由规则降级流程生成。
