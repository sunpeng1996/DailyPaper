---
title: 'FAMOS: Feed-Forward 3D Articulation Modeling from Sparse Observations'
title_zh: FAMOS：基于稀疏观测的前馈3D关节运动建模
authors:
- Kevin Qu
- Tao Sun
- Massimiliano Viola
- Liyuan Zhu
- Zhizhuo Zhou
- Sayan Deb Sarkar
- Konrad Schindler
- Iro Armeni
affiliations:
- Stanford University
- ETH Zurich
arxiv_id: '2609.20817'
url: https://arxiv.org/abs/2609.20817
pdf_url: https://arxiv.org/pdf/2609.20817
published: '2026-09-16'
collected: '2026-09-20'
category: Other
direction: 3D关节物体建模 · 稀疏观测推理
tags:
- 3D-Vision
- Articulation-Modeling
- Transformer
- Sparse-Observation
- Synthetic-Data
one_liner: 提出多态关节Transformer架构，从稀疏无序点云集预测可动部件分割与关节参数
practical_value: 主要是学术贡献，业务可借鉴点有限
score: 4
source: huggingface-daily
depth: abstract
---

### 动机
现有单观测前馈3D关节建模方法高度依赖类别级形状先验，同时公开数据集规模小、多样性不足，限制模型泛化能力。
### 方法关键点
1. 提出FAMOS前馈模型，支持可变数量输入（含单视角）的稀疏无序点云集联合推理，直接输出可动部件分割与关节参数；
2. 设计多态关节Transformer，交替采用状态级与全局注意力聚合跨观测的关节线索；
3. 新增观测关节跨度损失监督部件运动范围，引导模型充分利用全部观测信息；
4. 自研程序化数据生成器，训练时自动合成自带标注的样本扩充数据集。
### 关键结果
在PartNet-Mobility、ACD、ArtiCraft-10K三个数据集上，效果全面优于所有前馈及基于优化的基线方法。
