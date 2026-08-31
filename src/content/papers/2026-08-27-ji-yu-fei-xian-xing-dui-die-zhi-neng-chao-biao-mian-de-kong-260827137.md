---
title: Over-The-Air Extreme Learning Machines with Nonlinear Stacked Intelligent Metasurfaces
title_zh: 基于非线性堆叠智能超表面的空传极端学习机
authors:
- Kyriakos Stylianopoulos
- Mattia Fabiani
- Giulia Torcolacci
- Davide Dardari
- George C. Alexandropoulos
affiliations:
- 雅典国立卡波季斯特里安大学信息与电信系
- 博洛尼亚大学DEI
- 意大利CNIT无线通信国家实验室(WiLab)
arxiv_id: '2608.27137'
url: https://arxiv.org/abs/2608.27137
pdf_url: https://arxiv.org/pdf/2608.27137
published: '2026-08-27'
collected: '2026-08-31'
category: Other
direction: 空传机器学习 · 超表面硬件推理加速
tags:
- OTA_inference
- ELM
- XL_MIMO
- metasurface
- edge_inference
one_liner: 提出搭载级联超表面的XL MIMO系统，实现低复杂度波域空传二分类推理
practical_value: 主要是学术贡献，业务可借鉴点有限
score: 4
source: arxiv-cs.LG
depth: abstract
---

### 动机
面向目标导向通信范式下无线传输数据需直接执行机器学习推理的需求，解决传统边缘推理数据传输、计算开销高的痛点。
### 方法关键点
1 设计可作为Extreme Learning Machine (ELM)运行的超大规模MIMO（XL MIMO）架构，实现Over-The-Air (OTA)二分类；
2 接收机采用级联超表面+单射频链的低硬件复杂度设计，前置超表面层提供固定非线性响应作为ELM激活函数，后续可调线性超表面层直接在波域拟合训练好的网络权重。
### 关键结果
多数据集数值验证显示，该架构分类精度与理想数字模型相当，验证了低复杂度波域空传学习的可行性。
