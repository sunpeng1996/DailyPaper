---
title: Music Similarity Learning in Sparse Latin Scenarios
title_zh: 稀疏拉丁音乐场景下的音乐相似度学习方法
authors:
- Gabrielly Xavier dos Santos
- Lucas Dias Cler
- Olga Goussevskaia
affiliations:
- Universidade Federal de Minas Gerais (UFMG)
arxiv_id: '2611.22846'
url: https://arxiv.org/abs/2611.22846
pdf_url: https://arxiv.org/pdf/2611.22846
published: '2026-11-17'
collected: '2026-11-18'
category: RecSys
direction: 稀疏场景下跨文化物品相似度建模
tags:
- Collaborative Filtering
- Content-based Filtering
- Sparse Recommendation
- Zero-shot Evaluation
- Music Recommendation
one_liner: 结合内容过滤与协同过滤的轻量模型，零样本解决拉丁音乐稀疏场景相似度计算
practical_value: '- 长尾/小众垂类（如区域特色商品、小众内容）的相似度计算，可复用「公开属性+传统协同过滤」的轻量混合框架，规避多模态大模型的高算力与数据授权成本

  - 跨区域/跨文化的冷启推荐场景，可参考该方案的零样本泛化验证逻辑，提前评估模型对小众群体、小众品类的适配性

  - 可解释性要求高的推荐场景，优先选用传统过滤方法的混合架构，比黑盒深度/大模型方案更易满足合规审计要求'
score: 6
source: arxiv-cs.IR
depth: abstract
---

### 动机
当前主流音乐相似度建模依赖音频深度编码或多模态LLM方案，存在两大痛点：一是算力与数据门槛高，需授权音频数据、私有特征库及大额计算资源；二是训练数据偏倚西方英语品类，拉美等小众地域音乐的协同共现数据极稀疏，现有模型存在明显区域精度gap，无法适配小众文化场景。
### 方法关键点
1. 仅基于公开可获取的音乐元数据建模，无需音频信号处理步骤；
2. 轻量混合回归架构，结合经典item-based CF与内容过滤，完全可解释；
3. 采用零样本评估范式验证跨区域泛化能力。
### 关键结果
在稀疏拉美音乐零样本测试集上可准确预测未见item对的相似度，有效规避区域精度gap，算力成本远低于多模态深度方案
