---
title: Sim-to-Real Traffic Scene Understanding by Decoupling Semantics from Caption
  Generation with V-JEPA
title_zh: 基于V-JEPA解耦语义与字幕生成的仿真到真实交通场景理解
authors:
- Nguyen Hoai Thuong Bui
- Thanh Nguyen Vo
- Trinh Tra Giang Nguyen
- Ha Duc Bui
affiliations:
- Ho Chi Minh City University of Technology and Engineering (HCMUTE)
arxiv_id: '2609.18562'
url: https://arxiv.org/abs/2609.18562
pdf_url: https://arxiv.org/pdf/2609.18562
published: '2026-09-16'
collected: '2026-09-17'
category: Multimodal
direction: 多模态场景理解 · Sim2Real迁移
tags:
- V-JEPA
- Sim2Real
- VQA
- Caption Generation
- Multimodal
one_liner: 提出解耦语义与生成的交通场景理解框架，获2026 AI City Challenge Track 2冠军
practical_value: '- 解耦语义理解与生成的架构可复用在电商多模态商品文案、短视频旁白生成场景，先抽取商品/内容结构化属性再生成文本，可大幅降低生成幻觉

  - 训练-free的结构化语义修正机制可迁移到搜索Query理解、商品属性纠错、用户评论标签抽取任务，利用规则、关联关系、时序一致性修正模型预测误差，无额外训练成本

  - 冻结预训练大编码器+轻量下游预测头的选型思路，可在保留大模型强表征能力的同时降低下游任务微调成本，适合推荐系统多模态召回、广告素材理解等资源受限场景'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
AI City Challenge 2026 Track 2要求在sim2real域偏移场景下同时完成交通VQA与事件描述生成，现有视觉-语言方案将语义理解与生成耦合，易出现幻觉、跨事件阶段推理不一致问题。
### 方法关键点
1. 采用解耦架构：先将预设交通问题解析为结构化语义事实，再基于事实引导字幕生成；
2. 用冻结V-JEPA编码器提取预测性场景表征，搭配轻量Llama预测头输出VQA结果；
3. 引入无训练结构化修正机制，利用统计先验、问题间关联、时序事件一致性修正预测误差；
4. 修正后的语义事实输入Qwen3-VL-8B生成行人、车辆相关事件描述。
### 关键结果
官方基准测试VQA准确率达87.09%，总S2得分60.0853，位列所有参赛队伍第一。
