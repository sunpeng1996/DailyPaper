---
title: 'RSICCLLM: A Multimodal Large Language Model for Remote Sensing Image Change
  Captioning'
title_zh: 'RSICCLLM: A Multimodal Large Language Model for Re'
authors:
- Yelin Wang
- Zijia Song
- Shuo Ye
- Chuanguang Yang
- Miaoyu Wang
- Yong Xu
- Zhulin An
- Yongjun Xu
- Zitong Yu
arxiv_id: '2606.28266'
url: https://arxiv.org/abs/2606.28266
pdf_url: https://arxiv.org/pdf/2606.28266
published: '2026-06-26'
collected: '2026-06-29'
category: Multimodal
direction: Multimodal
tags:
- Multimodal
- LLM
one_liner: Remote Sensing Image Change Captioning (RSICC) aims to describe changes
  between bi-temporal rem...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 LLM API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 8
source: arxiv-cs.CV
depth: abstract
---

### 摘要

Remote Sensing Image Change Captioning (RSICC) aims to describe changes between bi-temporal remote sensing images and holds significant research and application value. However, most existing methods rely on conventional deep learning architectures, and the limited model capacity constrains performance. Although large-model post-training techniques have achieved great success in general domains, their direct transfer to RSICC remains challenging due to data scarcity and the need for fine-grained change understanding. To address this, we propose RSICCLLM, the first post-training framework for large vision-language models in RSICC. Specifically, we design a data generation paradigm, release the instruction dataset RSICI, and establish a task-specific RSICC benchmark. We further introduce Difference-aware Supervised Fine-tuning to explicitly extract change representations and guide the model in perceiving and understanding temporal differences. In addition, we propose Dual-Negative Preference Optimization (DNPO), which employs two complementary negative-sample construction strategies to construct the preference dataset RSICP and further refine model performance. Extensive experiments validate the superior capability of RSICCLLM, which achieves outstanding results with only 7B parameters, surpassing models of substantially larger scales. The code and dataset will be made publicly available at https://github.com/keaill/RSICCLLM.

> 当前运行未检测到 LLM API Key，本卡片由规则降级流程生成。
