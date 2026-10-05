---
title: Octrees as an Explicit 3D Language
title_zh: 以八叉树为显式3D语言的多模态大模型OctLLM
authors:
- Ran Dan
- Si-Tong Wei
- Pengfei Xiong
- Wei Zhang
- Yadong Mu
- Peng-Shuai Wang
affiliations:
- Peking University
- Independent Researcher
arxiv_id: '2610.02388'
url: https://arxiv.org/abs/2610.02388
pdf_url: https://arxiv.org/pdf/2610.02388
published: '2026-09-30'
collected: '2026-10-05'
category: LLM
direction: 多模态LLM · 3D模态适配
tags:
- Multimodal LLM
- Octree
- 3D Generation
- 3D Understanding
- Parameter Efficient Tuning
one_liner: 基于稀疏八叉树3D token与模态独立分支的OctLLM，兼顾3D任务性能与通用语言能力
practical_value: '- 新增垂直模态（如电商3D商品、工业结构化数据）适配LLM时，可复用「独立训练分支+共享自注意力」架构，不改动预训练主干，既保留原有通用能力，又大幅降低训练成本

  - 高维结构化数据（如用户长行为序列、商品多属性组合）token化可借鉴S-Octree的保结构压缩思路，在不损失核心信息的前提下降低序列长度，减少训练/推理开销

  - 涉及3D商品生成、AR试穿/试摆、3D商品语义理解的电商业务，可直接复用S-Octree的3D token化方案，快速基于现有LLM搭建3D相关能力'
score: 6
source: huggingface-daily
depth: abstract
---

## 动机
现有3D大模型存在两大缺陷：一是将3D形状压缩为隐式编码或坐标文本会丢失空间结构信息；二是通过全微调/LoRA引入3D模态时，要么训练成本极高，要么会覆盖主干原有通用语言能力，LoRA还存在模态容量不足的问题。
## 方法关键点
1. 稀疏八叉树（S-Octree）通过随机清空八叉树倒数第二层节点并删除后代节点，在保留形状结构的前提下压缩序列长度，生成带坐标、深度锚点的显式3D占用token序列；
2. 模态独立分支架构下新增独立可训练分支处理3D mesh token，文本、图像通路完全冻结，不同模态token通过共享自注意力层实现交互，不修改原有预训练语言通路。
## 关键结果
训练参数量远低于全微调方案，相比基线ShapeLLM-Omni，图像转3D FID降低17.4%，渲染相关描述生成指标提升28.7分，通用语言基准性能与预训练主干完全持平。
