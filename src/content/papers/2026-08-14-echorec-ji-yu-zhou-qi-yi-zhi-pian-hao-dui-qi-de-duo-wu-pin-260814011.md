---
title: 'EchoRec: Multi-Item Prediction-Empowered Generative Recommendation via Cycle-Consistent
  Preference Alignment'
title_zh: EchoRec：基于周期一致偏好对齐的多物品预测生成式推荐
authors:
- Haokai Ma
- Aoqi Hu
- Yueao Xing
- Ruobing Xie
- Yonghui Yang
- Teng Tu
- Lei Meng
- Tat-Seng Chua
affiliations:
- National University of Singapore
- Beijing University of Posts and Telecommunications
- Tencent
- Shandong University
arxiv_id: '2608.14011'
url: https://arxiv.org/abs/2608.14011
pdf_url: https://arxiv.org/pdf/2608.14011
published: '2026-08-14'
collected: '2026-08-17'
category: GenRec
direction: 生成式推荐 · Multi-Token Prediction
tags:
- Generative Recommendation
- Multi-Token Prediction
- Cycle Consistency
- Semantic ID
- Preference Alignment
one_liner: 利用链式多Token预测与周期一致偏好对齐挖掘未来行为监督信号，无推理开销提升生成式推荐性能
practical_value: '- 训练阶段可复用链式多分支MTP结构挖掘用户多步未来行为的免费监督信号，所有辅助分支推理时直接丢弃，不增加线上服务开销，适配电商推荐重训练轻推理的场景

  - 做跨空间表示对齐时可引入双向周期一致性约束，避免单向投影的伪对齐问题，无需额外标注就能提升对齐可靠性，可迁移到召回、多模态融合等任务

  - EchoRec为插件式框架，可直接接入RPG、SETRec等现有主流生成式推荐的训练流程，无需修改原有推理链路即可获得10%左右的效果提升，落地成本极低

  - 若业务需要做多步序列推荐（如购物路径预测、连续内容推流），可直接复用HPG模块的多分支输出，无需额外训练多模型即可生成非冗余的连贯多步推荐结果'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有生成式推荐引入Multi-Token Prediction(MTP)仅利用其解码效率优势，未挖掘其作为未来行为密集监督信号的潜力；并行MTP结构无视用户意图演化，导致多horizon预测同质化，且单向表示对齐存在无法验证的伪对齐问题，无法保证未来信号被有效吸收。

### 方法关键点
- 设计Horizon-aware Preference Generation(HPG)模块：链式堆叠轻量辅助MTP分支，每个分支基于上一分支输出预测下一horizon的物品，复用共享输出头与解码图，建模用户意图动态演化，仅增加少量训练开销
- 设计Verifiable Holistic-Preference Alignment(VHA)模块：聚合多分支偏好得到整体偏好表示，引入双向投影的周期一致性约束，理论上排除秩坍塌形式的伪对齐，保证解码表示真正吸收多步偏好信息；所有投影器训练后可丢弃，无推理开销
- 整体训练损失由多分支MTP损失与对齐损失加权组成，推理时仅保留基础MTP分支，完全兼容原有生成式推荐推理链路

### 关键结果
在Amazon Game、Baby、Arts三个高稀疏度公开数据集上，分别接入RPG、SETRec两个主流生成式推荐backbone验证，相对base最高获得21.4%的NDCG@10提升，平均提升幅度超10%；推理延迟、显存占用与原backbone完全一致，训练延迟仅提升1-2倍（训练阶段可接受）

### 核心洞见
用户未来交互行为蕴含当前偏好的语义回声，是完全免费的监督信号，只要解决好多步依赖建模与对齐有效性问题，就能在不增加推理成本的前提下显著提升推荐效果
