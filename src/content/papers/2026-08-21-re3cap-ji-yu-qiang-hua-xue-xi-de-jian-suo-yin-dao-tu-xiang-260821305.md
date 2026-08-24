---
title: 'Re$^3$Cap: Retrieval-Guided Refinement for Image Captioning Enhancement via
  Reinforcement Learning'
title_zh: Re³Cap：基于强化学习的检索引导图像描述生成优化方法
authors:
- Haonan Jia
- Shichao Dong
- Zenghui Sun
- Jiawen Zheng
- Ziqi Miao
- Gege Shi
- Qiuyu Zhao
- Jinsong Lan
- Xiaoyong Zhu
- Bo Zheng
affiliations:
- Taobao & Tmall Group of Alibaba
- The Hong Kong University of Science and Technology (Guangzhou)
- Shanghai Artificial Intelligence Laboratory
arxiv_id: '2608.21305'
url: https://arxiv.org/abs/2608.21305
pdf_url: https://arxiv.org/pdf/2608.21305
published: '2026-08-21'
collected: '2026-08-24'
category: Multimodal
direction: 多模态大模型 · 图像描述生成优化
tags:
- LVLM
- Image Captioning
- Reinforcement Learning
- Multimodal Retrieval
- Fine-tuning
one_liner: 结合多模态检索信号与强化学习，无额外标注提升LVLM图像描述准确率与丰富度
practical_value: '- 电商商品图自动生成详情文案/卖点场景，可复用CRS+CQA的检索-评估双模块架构，无需额外标注即可优化生成文案准确性，减少幻觉

  - 强化学习优化生成任务时，可引入同域多模态检索结果作为推理信号，弥补纯RL探索能力不足的问题，缩小与SFT的性能gap

  - 商品内容标签/多模态搜索召回场景，可复用该方法自动生成高质量图像标注，大幅降低人工标注成本'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有基于RL的LVLM图像描述优化方案探索能力不足，生成结果易出现幻觉、信息遗漏，性能与SFT存在明显差距，且大多依赖额外标注，落地成本高。
### 方法关键点
提出无额外标注需求的Re³Cap检索引导推理策略，包含两个核心模块：① Caption Refinement Suggester（CRS）：以多模态检索得到的相似图像对应高质量描述为信号，定位原始caption的幻觉与遗漏点，输出优化建议；② Caption Quality Assessor（CQA）：基于RL对优化后caption的质量做评估，迭代引导生成更准确、细节更丰富的描述。
### 关键结果
在COCO-LN500基准的关系推理任务上，Re³Cap比GRPO平均性能提升8.64%，整体效果优于SFT方案
