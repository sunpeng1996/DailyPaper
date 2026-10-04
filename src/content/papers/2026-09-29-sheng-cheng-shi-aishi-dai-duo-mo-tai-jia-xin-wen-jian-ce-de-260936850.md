---
title: Rethinking Multimodal Fake News Detection in the Generative AI Era
title_zh: 生成式AI时代多模态假新闻检测的再思考
authors:
- Wenbin Shen
- Guoxuan Qin
- Guangxu Yao
- Baodong Wang
- Yuanbo Rui
- Zhichao Lian
affiliations:
- Nanjing University of Science and Technology
- University of Chinese Academy of Sciences
arxiv_id: '2609.36850'
url: https://arxiv.org/abs/2609.36850
pdf_url: https://arxiv.org/pdf/2609.36850
published: '2026-09-29'
collected: '2026-10-04'
category: Other
direction: 多模态假新闻检测 · AIGC联合识别
tags:
- multimodal learning
- fake news detection
- AIGC detection
- hierarchical reasoning
one_liner: 构建生成内容场景多模态假新闻数据集Weibo26，提出感知生成性的分层推理框架GAHR
practical_value: '- 内容风控场景可复用「生成性感知+全局+局部分层推理」架构，无需部署独立的AIGC检测和假新闻检测两个模型，降低推理成本

  - 电商UGC/商家宣传内容造假检测可借鉴该思路，结合内容生成属性判断可信度，有效识别AI生成的虚假营销素材

  - 跨模态内容核验任务可参考Weibo26的标注逻辑，补充生成内容与原生内容混合场景的标注规则，提升数据集适配性'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有多模态假新闻检测仅聚焦内容真实性判断，AIGC检测仅能识别内容是否为生成模型产出，两类任务完全割裂，无法适配AIGC时代原生内容与生成内容混合的复杂假新闻场景。
### 方法关键点
1. 构建面向生成内容场景的中文多模态假新闻数据集Weibo26，覆盖原生+AIGC混合的多种假新闻形态，补全现有数据集缺失的生成属性标注
2. 提出Generativity-Aware Hierarchical Reasoning（GAHR）框架，采用「全局真实性判断+局部生成内容证据权重修正」的分层推理逻辑，将生成性特征纳入真实性推理链路
### 关键结果
在多个公开假新闻检测基准及Weibo26数据集上测试，GAHR真实性检测性能达到同期最优水平，同时可精准识别生成类内容，兼顾两类任务需求
