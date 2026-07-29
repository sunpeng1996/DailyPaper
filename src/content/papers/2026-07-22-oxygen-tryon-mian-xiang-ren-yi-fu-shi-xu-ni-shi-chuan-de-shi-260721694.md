---
title: 'Oxygen-TryOn: Fashion-Native Foundation Model for Any-item Virtual Try-On'
title_zh: Oxygen-TryOn：面向任意服饰虚拟试穿的时尚原生基础模型
authors:
- Yong Liu
- Xiaolong Fu
- Zihang Xu
- Wen Xue
- Xueheng Li
- Lin Song
- Yuan Zhang
- Chuyang Zhao
- Haoyang Huang
- Nan Duan
affiliations:
- Oxygen AIGC Group, JD
- Joy Future Academy, JD
arxiv_id: '2607.21694'
url: https://arxiv.org/abs/2607.21694
pdf_url: https://arxiv.org/pdf/2607.21694
published: '2026-07-22'
collected: '2026-07-29'
category: Multimodal
direction: 多模态生成 · 电商虚拟试穿
tags:
- Virtual Try-On
- Multimodal Generation
- Fashion AI
- Foundation Model
- RLHF
- E-commerce AI
one_liner: 打造时尚原生全品类虚拟试穿基础模型，效果超现有SOTA开源闭源方案
practical_value: '- 电商服饰场景可直接复用CPT+SFT+RL三阶段训练范式，RL阶段混合领域专属奖励+通用奖励的思路可大幅降低生成内容不符合业务要求的比例

  - 可参考其专用数据引擎的构建逻辑，规模化生产、标注虚拟试穿领域的高质量训练数据，解决领域训练数据稀缺的痛点

  - 无需mask补全的多参考理解式生成方案，可迁移至电商商品图生成、智能穿搭推荐、数字人直播穿搭定制等场景'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
现有虚拟试穿方案多复用通用图像编辑器，易出现服饰细节幻觉、人物身份漂移、纹理还原度差问题，且大多仅支持单品类、单服饰、棚拍场景，无法满足电商全品类、多场景试穿需求。
### 方法关键点
1. 重定义试穿为多参考理解驱动的生成任务，替代传统mask补全方案，可自主处理遮挡、服饰形变、叠穿逻辑，泛化性更强；
2. 搭建专用数据引擎，规模化完成试穿数据的采集、生成、标注、过滤，保障训练数据质量；
3. 采用持续预训练(CPT)+监督微调(SFT)+强化学习(RL)三阶段训练，RL阶段混合自研试穿专属奖励模型与规则引导的通用奖励，同时支持试穿任务与通用图像编辑指令响应。
### 关键结果
在公开基准及自有测试集上，单物品试穿的一致性、真实感达SOTA，多物品试穿效果领先，匹配或超越Nano Banana Pro、GPT-Image-2、Seedream5 Lite等闭源方案及FLUX.2开源模型。
