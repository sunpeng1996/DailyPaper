---
title: 'The Price of Isolation: Estimating the Ecosystem Cost of Symmetric Two-Sided
  A/B Testing'
title_zh: 隔离的代价：双边对称A/B测试的生态成本估算
authors:
- Yuanyuan Shen
- Yiren Yan
- Wenjie Li
- Chunhui Zhu
affiliations:
- Snap Inc.
arxiv_id: '2608.04432'
url: https://arxiv.org/abs/2608.04432
pdf_url: https://arxiv.org/pdf/2608.04432
published: '2026-08-05'
collected: '2026-08-06'
category: RecSys
direction: 推荐系统 · 双边平台A/B测试优化
tags:
- A-B-testing
- two-sided-marketplace
- recommender-system
- extreme-value-theory
- marketplace-interference
one_liner: 基于极值理论量化双边平台隔离A/B测试的流量损耗，给出预评估流程与流量分配方案
practical_value: '- 双边平台做创作者侧/冷启动隔离A/B测试前，先基于内容匹配质量的尾部分布估算损耗，避免盲目切流量导致用户体验下跌

  - 若平台匹配质量为长尾分布，无需盲目扩大总池容量降低隔离损耗，直接参考论文预飞流程调整测试流量占比或换实验方案

  - 可复用极值理论建模方法量化推荐候选池收缩带来的engagement损失，用于其他流量拆分场景的成本估算'
score: 7
source: arxiv-cs.IR
depth: abstract
---

### 动机
双边内容平台普遍采用对称隔离A/B测试消除创作者侧、冷启动实验的跨组市场干扰，但隔离会缩窄用户候选内容池，行业默认平台规模越大该损耗越低，缺乏科学的量化与预评估方法。
### 方法关键点
基于订单统计模型与极值理论建模用户-内容匹配质量的尾部分布，得到明确的二分损耗规律：轻尾/有界尾分布下损耗随候选池扩容逐渐消失，重尾分布下损耗收敛为与池规模无关的常数；同时给出可落地上线前预飞流程，可提前估算隔离成本、确定测试流量占比，成本超阈值时自动推荐替代实验设计。
### 关键结果
千万级创作者规模的生产实验验证：A/A流量扫测可检测到梯度式的engagement损耗；小探索池校准的尾部指数预测值与全量候选池消融实验观测值高度一致；重尾场景下即使将候选池扩大数个量级也无法消除隔离损耗。
