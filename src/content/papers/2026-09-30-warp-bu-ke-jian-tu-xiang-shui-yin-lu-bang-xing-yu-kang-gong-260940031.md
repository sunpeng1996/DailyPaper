---
title: 'WARP: A Unified Benchmark for Invisible Image Watermarking -- Robustness and
  Protection Against Attacks'
title_zh: WARP：不可见图像水印鲁棒性与抗攻击能力统一评测基准
authors:
- Khaled Abud
- Aleksey Yakushev
- Aleksandr Akimenkov
- Irina Serzhenko
- Kirill Aistov
- Egor Kovalev
- Dmitry Obydenkov
- Sergey Lavrushkin
- Anastasia Antsiferova
- Dmitriy Vatolin
affiliations:
- MSU Institute for Artificial Intelligence
- Trusted AI Research Center RAS
- Independent researcher
arxiv_id: '2609.40031'
url: https://arxiv.org/abs/2609.40031
pdf_url: https://arxiv.org/pdf/2609.40031
published: '2026-09-30'
collected: '2026-10-04'
category: Eval
direction: 不可见图像水印 · 鲁棒性评测基准
tags:
- Watermarking
- Benchmark
- AIGC Governance
- Robustness Evaluation
- Image Security
one_liner: 推出覆盖32种水印方法、34种攻击方式的不可见图像水印统一评测基准WARP
practical_value: '- 电商AIGC商品图/营销素材溯源场景，可直接用WARP的攻击测试集验证水印方案的抗篡改能力，避开仅抗常规失真但易被重嵌入攻击破解的方案

  - 素材版权防护场景可参考WARP的评测结论，优先选择同时抗常规畸变、对抗攻击、重嵌入攻击的水印方法，降低盗图侵权风险

  - 自研业务专属水印方案时，可复用WARP的标准化评测流程快速迭代，无需自行搭建全量攻击测试框架'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
AIGC内容溯源合规需求激增，现有不可见图像水印评测基准未覆盖最新水印技术与对抗、重嵌入等新型攻击，缺乏统一可复现的评测标准。
### 方法关键点
1. 推出WARP统一评测框架，纳入32种经典、深度、生成式水印方法，以及34种擦除攻击（覆盖传统畸变、对抗攻击、净化攻击、重嵌入攻击全场景）
2. 提供感知质量、水印可读性、抗攻击能力三类标准化、可扩展的评测协议
### 关键结果
1. 产出当前领域规模最大的不可见水印鲁棒性评测数据集
2. 明确了不同水印方法与对应最高效攻击策略的稳定关联关系
3. 发现部分对常规失真鲁棒的水印方案，对重嵌入攻击的脆弱性极高
